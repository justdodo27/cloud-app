from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func, case
import models
import schemas
from uuid import uuid4
from typing import List

app = FastAPI()

def get_db():
    db = models.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/objects/", response_model=List[schemas.FoodItemSchema])
def read_food_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    food_items = db.query(models.FoodItem).offset(skip).limit(limit).all()
    return food_items


@app.get("/object/", response_model=List[schemas.FoodItemSchema])
def read_food_item_by_name(name: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    food_items = db.query(models.FoodItem)\
                   .filter(models.FoodItem.descrip.match(name))\
                   .order_by(func.similarity(models.FoodItem.descrip, name).desc())\
                   .offset(skip).limit(limit).all()
    if not food_items:
        raise HTTPException(status_code=404, detail="Food item not found")
    return food_items


@app.post("/object/", response_model=schemas.FoodItemSchema)
def create_food_item(food_item: schemas.FoodItemCreate, db: Session = Depends(get_db)):
    db_food_item = models.FoodItem(**food_item.model_dump(), ndb_no=str(uuid4()))
    db.add(db_food_item)
    db.commit()
    db.refresh(db_food_item)
    return db_food_item


@app.put("/object/{food_item_id}", response_model=schemas.FoodItemSchema)
def update_food_item(food_item_id: str, food_item: schemas.FoodItemUpdate, db: Session = Depends(get_db)):
    db_food_item = db.query(models.FoodItem).filter(models.FoodItem.ndb_no == food_item_id).first()
    if db_food_item is None:
        raise HTTPException(status_code=404, detail="Food item not found")
    for var, value in vars(food_item).items():
        setattr(db_food_item, var, value) if value else None
    db.commit()
    return db_food_item


@app.get("/stats/")
def food_nutrient_stats(db: Session = Depends(get_db)):
    stats = {
        "average_nutrients": {
            "energy_kcal": db.query(func.avg(models.FoodItem.energy_kcal)).scalar(),
            "protein_g": db.query(func.avg(models.FoodItem.protein_g)).scalar(),
            "fat_g": db.query(func.avg(models.FoodItem.fat_g)).scalar(),
            "carb_g": db.query(func.avg(models.FoodItem.carb_g)).scalar(),
        },
        "min_nutrients": {
            "energy_kcal": db.query(func.min(models.FoodItem.energy_kcal)).scalar(),
            "protein_g": db.query(func.min(models.FoodItem.protein_g)).scalar(),
            "fat_g": db.query(func.min(models.FoodItem.fat_g)).scalar(),
            "carb_g": db.query(func.min(models.FoodItem.carb_g)).scalar(),
        },
        "max_nutrients": {
            "energy_kcal": db.query(func.max(models.FoodItem.energy_kcal)).scalar(),
            "protein_g": db.query(func.max(models.FoodItem.protein_g)).scalar(),
            "fat_g": db.query(func.max(models.FoodItem.fat_g)).scalar(),
            "carb_g": db.query(func.max(models.FoodItem.carb_g)).scalar(),
        }
    }
    
    # Define thresholds for categorization
    high_threshold = 10.0
    low_threshold = 5.0

    # Conditional aggregation for energy density categories
    energy_density_stats = db.query(
        func.sum(case((models.FoodItem.energy_kcal / models.FoodItem.carb_g > high_threshold, 1), else_=0)).label('high'),
        func.sum(case((models.FoodItem.energy_kcal / models.FoodItem.carb_g <= low_threshold, 1), else_=0)).label('low'),
        func.sum(case((models.FoodItem.energy_kcal / models.FoodItem.carb_g > low_threshold, 1), else_=0)).label('medium_or_high')
    ).filter(models.FoodItem.carb_g > 0).one()

    # Calculate medium by subtracting high from medium_or_high
    medium = energy_density_stats.medium_or_high - energy_density_stats.high

    stats["energy_density_distribution"] = {
        "high": energy_density_stats.high,
        "medium": medium,
        "low": energy_density_stats.low,
    }

    return stats


def calculate_nutrient_score(food_item: models.FoodItem):
    # Simple scoring example: prioritize protein and fiber, penalize high calories and saturated fats
    score = (food_item.protein_g * 2 + food_item.fiber_g * 2) - (food_item.energy_kcal * 0.1 + food_item.saturated_fats_g * 2)
    return score


@app.get("/healthy-foods/", response_model=List[schemas.FoodItemWithScoreSchema])
def get_healthy_foods(skip: int = Query(default=0, ge=0), limit: int = Query(default=10, ge=1), db: Session = Depends(get_db)):
    food_items = db.query(models.FoodItem).all()
    
    # Calculate nutrient score for each food item
    for food_item in food_items:
        food_item.nutrient_score = calculate_nutrient_score(food_item)
    
    # Sort food items based on their nutrient score, higher is better
    sorted_food_items = sorted(food_items, key=lambda x: x.nutrient_score, reverse=True)
    
    paginated_food_items = sorted_food_items[skip: skip + limit]
    
    return paginated_food_items