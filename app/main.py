from typing import Optional
from fastapi import FastAPI
from .fileHandler import getItems
from .dependencies.id import ID

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "200"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/list")
def get_list():
    items = getItems()
    return items