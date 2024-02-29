from pydantic import BaseModel
from typing import Optional

# Schema for request body of a new food item
class FoodItemCreate(BaseModel):
    descrip: str
    energy_kcal: Optional[float] = None
    protein_g: Optional[float] = None
    saturated_fats_g: Optional[float] = None
    fat_g: Optional[float] = None
    carb_g: Optional[float] = None
    fiber_g: Optional[float] = None
    sugar_g: Optional[float] = None
    calcium_mg: Optional[float] = None
    iron_mg: Optional[float] = None
    magnesium_mg: Optional[float] = None
    phosphorus_mg: Optional[float] = None
    potassium_mg: Optional[float] = None
    sodium_mg: Optional[float] = None
    zinc_mg: Optional[float] = None
    copper_mcg: Optional[float] = None
    manganese_mg: Optional[float] = None
    selenium_mcg: Optional[float] = None
    vitc_mg: Optional[float] = None
    thiamin_mg: Optional[float] = None
    riboflavin_mg: Optional[float] = None
    niacin_mg: Optional[float] = None
    vitb6_mg: Optional[float] = None
    folate_mcg: Optional[float] = None
    vitb12_mcg: Optional[float] = None
    vita_mcg: Optional[float] = None
    vite_mg: Optional[float] = None
    vitd2_mcg: Optional[float] = None

    class Config:
        from_attributes = True

# Schema for updating an existing food item, all fields are optional
class FoodItemUpdate(BaseModel):
    descrip: Optional[str] = None
    energy_kcal: Optional[float] = None
    protein_g: Optional[float] = None
    energy_kcal: Optional[float] = None
    protein_g: Optional[float] = None
    saturated_fats_g: Optional[float] = None
    fat_g: Optional[float] = None
    carb_g: Optional[float] = None
    fiber_g: Optional[float] = None
    sugar_g: Optional[float] = None
    calcium_mg: Optional[float] = None
    iron_mg: Optional[float] = None
    magnesium_mg: Optional[float] = None
    phosphorus_mg: Optional[float] = None
    potassium_mg: Optional[float] = None
    sodium_mg: Optional[float] = None
    zinc_mg: Optional[float] = None
    copper_mcg: Optional[float] = None
    manganese_mg: Optional[float] = None
    selenium_mcg: Optional[float] = None
    vitc_mg: Optional[float] = None
    thiamin_mg: Optional[float] = None
    riboflavin_mg: Optional[float] = None
    niacin_mg: Optional[float] = None
    vitb6_mg: Optional[float] = None
    folate_mcg: Optional[float] = None
    vitb12_mcg: Optional[float] = None
    vita_mcg: Optional[float] = None
    vite_mg: Optional[float] = None
    vitd2_mcg: Optional[float] = None

    class Config:
        from_attributes = True

# Schema for response model of a food item
class FoodItemSchema(FoodItemCreate):
    ndb_no: str  # Add the ID to the response model

    class Config:
        from_attributes = True


class FoodItemWithScoreSchema(FoodItemSchema):
    nutrient_score: float

    class Config:
        from_attributes = True