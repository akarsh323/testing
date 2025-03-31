from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

def test_get_existing_item():
    """Test getting an item that exists."""
    response = client.post("/items/", json={"item_id": "1"})
    assert response.status_code == 200
    assert response.json() == {"name": "Laptop", "price": 1200}
