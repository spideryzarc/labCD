import sqlite3 as sq
import os

from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLite database file
DB_FILE = "sqlite:///test.db"
# Create a SQLite engine
engine = create_engine(DB_FILE)
# Create a base class for declarative models
Base = declarative_base(bind=engine)

# Define costumers table  
class Costumers(Base):
    __tablename__ = "costumers"
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(50))
    email = Column(Unicode(50))
    address = Column(UnicodeText)
    latitude = Column(Float)
    longitude = Column(Float)
    


# Create the table if it doesn't exist
def create_table():
    if not os.path.exists("test.db"):
        Base.metadata.create_all(engine)
        print("Table created successfully.")
    else:
        print("Table already exists.")

if __name__ == "__main__":
    os.remove("test.db") if os.path.exists("test.db") else None
    create_table()
    # add a new costumer
    a = Costumers()
    a.name = "John Doe"
    a.address = "123 Main St"
    a.latitude = 40.7128
    a.longitude = -74.0060

    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(a)
    session.commit()
    session.close()
    # query the costumers table
    session = Session()
    costumers = session.query(Costumers).all()
    for costumer in costumers:
        print(costumer.name, costumer.address, costumer.latitude, costumer.longitude)
    session.close()

    