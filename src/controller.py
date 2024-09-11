import models
import db_conn
from schema import Item, ItemBase, ItemCreate

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

models.Base.metadata.create_all(bind=db_conn.engine)


@app.get('/')
def home():
    return {'Welcome to my fisrt API!': 'Agradecimentos ao prof. Galvão Filho!'}
        
@app.post("/items/", response_model=Item)
def create_item(item: ItemCreate, db: Session = Depends(db_conn.get_db)):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=List[Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(db_conn.get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(db_conn.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.delete("/items/{item_id}", response_model=Item)
def delete_item(item_id: int, db: Session = Depends(db_conn.get_db)):
    db_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

