from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Fake database
items = []

# -------------------------
# Pydantic Model
# -------------------------

class Item(BaseModel):
    text: str
    is_done: bool = False


# -------------------------
# Root Endpoint
# -------------------------

@app.get("/")
def root():
    return {"message": "Welcome to FastAPI TP3"}


# -------------------------
# Create Item (POST)
# -------------------------

@app.post("/items", response_model=list[Item])
def create_item(item: Item):
    items.append(item)
    return items


# -------------------------
# Get Specific Item (GET with Path Param)
# -------------------------

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(
            status_code=404,
            detail=f"Item {item_id} not found"
        )


# -------------------------
# List Items with Query Param
# -------------------------

@app.get("/items", response_model=list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

