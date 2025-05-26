from model import Session, Depots
from typing import Union, Optional

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

# Torna latitude e longitude opcionais no schema gerado
DepotsCreateSchema.__annotations__["latitude"] = Optional[float]
DepotsCreateSchema.__annotations__["longitude"] = Optional[float]
DepotsCreateSchema.latitude = None
DepotsCreateSchema.longitude = None

@app.post("/add_depot")
def add_depot(depot: DepotsCreateSchema, db: Session = Depends(get_db)):
    print("depot data:\n", depot)
    # search coordinates  if necessary
    if not depot.latitude or not depot.longitude:
        depot.latitude, depot.longitude = ox.geocode(depot.address)
    new_depot = Depots(**depot.dict())
    db.add(new_depot)
    db.commit()
    db.refresh(new_depot)
    print("Depot added to DB:\n", new_depot)
    return {"status": "success", "new_id": new_depot.id}


if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")
