from model import Session, Depots
from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import osmnx as ox

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

class Item(BaseModel):
    name: str
    age: int

@app.get("/echo")
def echo(x:Item):
    print("echo data:\n", x)
    return {"received_data": x}

class ValidDepot(BaseModel):
    name: str
    adress: str
    latitude: Union[float, None] = None
    longitude: Union[float, None] = None

@app.get("/add_depot")
def add_depot(depot: ValidDepot):
    print("depot data:\n", depot)
    if not depot.latitude or not depot.longitude:
        # search for depot coordinates
        depot.latitude, depot.longitude = ox.geocode(depot.adress)
    with Session() as session:
        depot_data = Depots(
            name=depot.name,
            address=depot.adress,
            latitude=depot.latitude,
            longitude=depot.longitude
        )
        session.add(depot_data)
        session.commit()
        session.refresh(depot_data)
    print("Depot added to DB:\n", depot_data)
    return {"status": "success", "data": depot_data}     

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")