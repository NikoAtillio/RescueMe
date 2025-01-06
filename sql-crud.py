from rescue_me.data_feed import (
     get_all_rescues, get_rescue_by_id, get_rescue_by_name, get_rescue_by_location, get_rescue_by_species, get_rescue_by_breed, get_rescue_by_age, get_rescue_by_size,
 )

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

# Update connection string with credentials
db = create_engine("postgresql://username:password@localhost/rescueme")
base = declarative_base()

# create a class-based model fot the rescues table
class Programmer(base):
    __tablename__ = "rescues"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    species = Column(String)
    breed = Column(String)
    age = Column(Integer)
    size = Column(String)


# instead of connecting to the database directly, we will create a session
# create a new instance of the sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on our Programmer table

# add each instance of our Programmer class to the session

# commit the session to the database

# query the database to retrieve all Programmers

