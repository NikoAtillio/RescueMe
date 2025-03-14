from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
import os
from datetime import date

# Database connection
db = create_engine(os.environ.get('DATABASE_URL'))
base = declarative_base()

# Enum for animal status
class AnimalStatus(enum.Enum):
    AVAILABLE = "Available"
    ADOPTED = "Adopted"
    FOSTERED = "Fostered"
    PENDING = "Pending"

# Animal Model
class Animal(base):
    """Model for animals in rescue database"""
    __tablename__ = "animals"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    species = Column(String(50), nullable=False)
    breed = Column(String(50))
    age = Column(Integer)
    gender = Column(String(10))
    size = Column(String(20))
    status = Column(Enum(AnimalStatus), default=AnimalStatus.AVAILABLE)
    arrival_date = Column(Date, default=date.today)
    description = Column(String(500))

# Session setup
Session = sessionmaker(db)
session = Session()

# Create tables
base.metadata.create_all(db)

def add_animal(name, species, breed=None, age=None, gender=None, size=None, description=None):
    """Add a new animal to the database"""
    try:
        animal = Animal(
            name=name,
            species=species,
            breed=breed,
            age=age,
            gender=gender,
            size=size,
            description=description
        )
        session.add(animal)
        session.commit()
        return animal
    except Exception as e:
        session.rollback()
        raise e

def get_all_animals():
    """Retrieve all animals from database"""
    return session.query(Animal).all()

def update_animal(animal_id, **kwargs):
    """Update animal details"""
    try:
        animal = session.query(Animal).filter_by(id=animal_id).first()
        if animal:
            for key, value in kwargs.items():
                setattr(animal, key, value)
            session.commit()
            return animal
        return None
    except Exception as e:
        session.rollback()
        raise e

def delete_animal(animal_id):
    """Delete animal from database"""
    try:
        animal = session.query(Animal).filter_by(id=animal_id).first()
        if animal:
            session.delete(animal)
            session.commit()
            return True
        return False
    except Exception as e:
        session.rollback()
        raise e

# Example usage:
if __name__ == "__main__":
    # Add animal
    new_animal = add_animal(
        name="Max",
        species="Dog",
        breed="Labrador",
        age=3,
        gender="Male",
        size="Large",
        description="Friendly and energetic"
    )

    # Update animal
    update_animal(new_animal.id, status=AnimalStatus.ADOPTED)

    # Get all animals
    all_animals = get_all_animals()
    for animal in all_animals:
        print(f"{animal.name} - {animal.species} - {animal.status.value}")
