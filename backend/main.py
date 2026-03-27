from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Beginner Python Backend")


class Item(BaseModel):
    name: str
    price: float


items = [
    {"id": 1, "name": "Book", "price": 10.0},
    {"id": 2, "name": "Pen", "price": 2.5},
]


@app.get("/")
def home():
    return {"message": "Welcome to your first Python backend!"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/items")
def get_items():
    return items


@app.post("/items")
def create_item(item: Item):
    new_item = {
        "id": len(items) + 1,
        "name": item.name,
        "price": item.price,
    }
    items.append(new_item)
    return {"message": "Item added", "item": new_item}
