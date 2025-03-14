from sqlalchemy import create_engine, Column, Integer, String, Date, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import enum
import os
from datetime import date

# Database connection
engine = create_engine(os.environ.get('DATABASE_URL'))
Base = declarative_base()

class AnimalStatus(enum.Enum):
    AVAILABLE = "Available"
    ADOPTED = "Adopted"
    FOSTERED = "Fostered"
    PENDING = "Pending"

class Animal(Base):
    __tablename__ = 'animals'
    
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

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create tables
Base.metadata.create_all(engine)
