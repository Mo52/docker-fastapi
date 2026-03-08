from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# ১. POST টেস্ট (আইডি সহ ডাটা তৈরি)
def test_create_item():
    # আপনার রুটে /items/{item_id} আছে, তাই এখানে /items/1 ব্যবহার করা হয়েছে
    response = client.post("/items/1", json={"name": "Test Item", "price": 100.0})
    assert response.status_code == 200
    assert response.json() == {"message": "Saved to Database!"}

# ২. GET টেস্ট (সব ডাটা পড়া)
def test_get_all_items():
    # আপনার রুটে আইডি ছাড়া শুধু /items/ আছে সব ডাটা দেখার জন্য
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# ৩. PUT টেস্ট (ডাটা আপডেট করা)
def test_update_item():
    response = client.put("/items/1", json={"name": "Updated Item", "price": 150.0})
    assert response.status_code == 200
    assert response.json() == {"message": "Updated in Database!"}

# ৪. DELETE টেস্ট (ডাটা মুছে ফেলা)
def test_delete_item():
    response = client.delete("/items/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Deleted from Database!"}
