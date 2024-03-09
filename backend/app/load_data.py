import csv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models import Base, FoodItem
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_activate_library():
    db = SessionLocal()
    db.execute(text('CREATE EXTENSION IF NOT EXISTS pg_trgm'))
    db.commit()


def load_data(csv_file_path):
    db = SessionLocal()
    Base.metadata.create_all(bind=engine)
    db.commit()

    with open(csv_file_path, newline='') as csvfile:
        data_reader = csv.DictReader(csvfile)
        for row in data_reader:
            food_item = FoodItem(
                ndb_no=row['NDB_No'],
                descrip=row['Descrip'],
                energy_kcal=float(row['Energy_kcal']),
                protein_g=float(row['Protein_g']),
                saturated_fats_g=float(row['Saturated_fats_g']),
                fat_g=float(row['Fat_g']),
                carb_g=float(row['Carb_g']),
                fiber_g=float(row['Fiber_g']),
                sugar_g=float(row['Sugar_g']),
                calcium_mg=float(row['Calcium_mg']),
                iron_mg=float(row['Iron_mg']),
                magnesium_mg=float(row['Magnesium_mg']),
                phosphorus_mg=float(row['Phosphorus_mg']),
                potassium_mg=float(row['Potassium_mg']),
                sodium_mg=float(row['Sodium_mg']),
                zinc_mg=float(row['Zinc_mg']),
                copper_mcg=float(row['Copper_mcg']),
                manganese_mg=float(row['Manganese_mg']),
                selenium_mcg=float(row['Selenium_mcg']),
                vitc_mg=float(row['VitC_mg']),
                thiamin_mg=float(row['Thiamin_mg']),
                riboflavin_mg=float(row['Riboflavin_mg']),
                niacin_mg=float(row['Niacin_mg']),
                vitb6_mg=float(row['VitB6_mg']),
                folate_mcg=float(row['Folate_mcg']),
                vitb12_mcg=float(row['VitB12_mcg']),
                vita_mcg=float(row['VitA_mcg']),
                vite_mg=float(row['VitE_mg']),
                vitd2_mcg=float(row['VitD2_mcg']),
            )
            db.add(food_item)
            db.commit()
    db.close()