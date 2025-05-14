from model import Session, Depots
from typing import Union

import osmnx as ox
import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from pydantic_sqlalchemy import sqlalchemy_to_pydantic

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


DepotsCreateSchema = sqlalchemy_to_pydantic(Depots, exclude=["id"])


@app.get("/add_depot")
def add_depot(depot: DepotsCreateSchema, db: Session = Depends(get_db)):
    print("depot data:\n", depot)
    # search coordinates  if necessary
    if not depot.latitude or not depot.longitude:
        print("searching coordinates for address:\n", depot.address)
        depot.latitude, depot.longitude = ox.geocode(depot.address)
        print("found coordinates:\n", depot.latitude, depot.longitude)
    new_depot = Depots(**depot.dict())
    db.add(new_depot)
    db.commit()
    db.refresh(new_depot)
    print("Depot added to DB:\n", new_depot)
    return {"status": "success", "new_entry": new_depot}

@app.get("/get_depots")
def get_depots(db: Session = Depends(get_db)):
    depots = db.query(Depots).all()
    print("depot data:\n", depots)
    return {"status": "success", "depot_data": depots}

@app.get("/get_depot/{depot_id}")
def get_depot(depot_id: int, db: Session = Depends(get_db)):
    depot = db.query(Depots).filter(Depots.id == depot_id).first()
    if not depot:
        return {"status": "error", "message": "Depot not found"}
    print("depot data:\n", depot)
    return {"status": "success", "depot_data": depot}

@app.get("/delete_depot/{depot_id}")
def delete_depot(depot_id: int, db: Session = Depends(get_db)):
    #set to inactive
    depot = db.query(Depots).filter(Depots.id == depot_id).first()
    if not depot:
        return {"status": "error", "message": "Depot not found"}
    if depot.is_active:
        depot.is_active = False
        db.commit()
        db.refresh(depot)
        print("Depot deleted:\n", depot)
        return {"status": "success", "depot_data": depot}
    else:
        return {"status": "error", "message": "Depot already inactive"}
    
@app.get("/tester")
def test_func(data:dict):
    print("input:\n", data)
    return {"status": "success", "input": data}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
