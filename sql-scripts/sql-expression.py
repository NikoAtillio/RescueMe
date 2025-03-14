from sqlalchemy import (
    create_engine, Table, Column, Integer, String, MetaData, Enum, Date
)
import os
from datetime import date
import enum

# Database connection
engine = create_engine(os.environ.get('DATABASE_URL'))

# Create a metadata instance
meta = MetaData()

# Define AnimalStatus enum
class AnimalStatus(enum.Enum):
    AVAILABLE = "Available"
    ADOPTED = "Adopted"
    FOSTERED = "Fostered"
    PENDING = "Pending"

# Create the animals table
animals = Table(
    "animals", meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("species", String(50), nullable=False),
    Column("breed", String(50)),
    Column("age", Integer),
    Column("gender", String(10)),
    Column("size", String(20)),
    Column("status", Enum(AnimalStatus)),
    Column("arrival_date", Date),
    Column("description", String(500))
)

# Create tables
meta.create_all(engine)

# Example queries
with engine.connect() as conn:
    # Insert
    conn.execute(animals.insert().values(
        name="Max",
        species="Dog",
        breed="Labrador",
        age=3
    ))
    
    # Select
    select_st = animals.select()
    result = conn.execute(select_st)
    
    # Update
    update_st = animals.update().where(animals.c.name=="Max")\
                              .values(status="Adopted")
    conn.execute(update_st)