from sqlalchemy import Column, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/dbname")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class FoodItem(Base):
    __tablename__ = "food_items"

    ndb_no = Column(String, primary_key=True, index=True)
    descrip = Column(String)
    energy_kcal = Column(Float)
    protein_g = Column(Float)
    saturated_fats_g = Column(Float)
    fat_g = Column(Float)
    carb_g = Column(Float)
    fiber_g = Column(Float)
    sugar_g = Column(Float)
    calcium_mg = Column(Float)
    iron_mg = Column(Float)
    magnesium_mg = Column(Float)
    phosphorus_mg = Column(Float)
    potassium_mg = Column(Float)
    sodium_mg = Column(Float)
    zinc_mg = Column(Float)
    copper_mcg = Column(Float)
    manganese_mg = Column(Float)
    selenium_mcg = Column(Float)
    vitc_mg = Column(Float)
    thiamin_mg = Column(Float)
    riboflavin_mg = Column(Float)
    niacin_mg = Column(Float)
    vitb6_mg = Column(Float)
    folate_mcg = Column(Float)
    vitb12_mcg = Column(Float)
    vita_mcg = Column(Float)
    vite_mg = Column(Float)
    vitd2_mcg = Column(Float)
