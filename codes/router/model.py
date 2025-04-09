from sqlalchemy import Column, Integer, Unicode, UnicodeText, String, Float, Boolean
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Create a SQLite engine
engine = create_engine("sqlite:///router.db")
# Create a base class for declarative models
Base = declarative_base(bind=engine)
# Create a session factory
Session = sessionmaker(bind=engine)

# Define costumers table
class Costumers(Base):
    __tablename__ = "costumers"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True, index=True)
    address = Column(UnicodeText)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    active = Column(Boolean, default=True)
    orders = relationship("Orders", back_populates="customer")

# Define vehicles table
class Vehicles(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    model = Column(String(100))
    plate = Column(String(10), unique=True, index=True, nullable=False)
    capacity = Column(Integer, nullable=False)
    cost_per_km = Column(Float, default=1.0)
    active = Column(Boolean, default=True)

# Define orders table
class Orders(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True)
    status = Column(String(50), default="pending")
    demand = Column(Integer, nullable=False, default=1)
    customer_id = Column(Integer, ForeignKey("costumers.id"), nullable=False)
    customer = relationship("Costumers", back_populates="orders")


Base.metadata.create_all(engine)

if __name__ == "__main__":
    # clean the database
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # list all tables
    print(Base.metadata.tables.keys())
    # create a session
    session = Session()
    # add a new costumer
    a = Costumers()
    a.name = "John Doe"
    a.address = "123 Main St"
    a.email = "a@a.com"
    a.latitude = 40.7128
    a.longitude = -74.0060
    session.add(a)
    session.commit()
    # add a new vehicle
    b = Vehicles()
    b.model = "Toyota"
    b.plate = "ABC123"
    b.capacity = 1000
    b.cost_per_km = 1.0
    session.add(b)
    session.commit()
    # add a new order
    c = Orders()
    c.status = "pending"
    c.demand = 10
    c.customer_id = a.id
    session.add(c)
    session.commit()
    # add a new order
    d = Orders()
    d.status = "pending"
    d.demand = 20
    d.customer_id = a.id
    session.add(d)
    session.commit()
    # query the costumers table
    costumers = session.query(Costumers).all()
    for costumer in costumers:
        print(costumer.name, costumer.address, costumer.latitude, costumer.longitude)
    # query the vehicles table
    vehicles = session.query(Vehicles).all()
    for vehicle in vehicles:
        print(vehicle.model, vehicle.plate, vehicle.capacity, vehicle.cost_per_km)
    # query the orders table
    orders = session.query(Orders).all()
    for order in orders:
        print(order.status, order.demand, order.customer.name)

    # close the session
    session.close()
