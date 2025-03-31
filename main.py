from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# Sample dictionary to store data
items = {
    "1": {"name": "Laptop", "price": 1200},
    "2": {"name": "Phone", "price": 800},
    "3": {"name": "Tablet", "price": 500},
}

# Request model
class ItemRequest(BaseModel):
    item_id: str

@app.post("/items/")
async def get_item(request: ItemRequest):
    if request.item_id in items:
        return items[request.item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)