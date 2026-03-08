from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# test
# ডাটাবেস টেবিল তৈরি করা
def init_db():
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

class Item(BaseModel):
    name: str
    price: float

# ১. GET (পড়া) - নীল রঙ
@app.get("/items/")
def get_items():
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "price": r[2]} for r in rows]

# ২. POST (তৈরি করা) - সবুজ রঙ
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO items (id, name, price) VALUES (?, ?, ?)",
                       (item_id, item.name, item.price))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="ID already exists")
    conn.close()
    return {"message": "Saved to Database!"}

# ৩. PUT (আপডেট করা) - কমলা রঙ
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name = ?, price = ? WHERE id = ?",
                   (item.name, item.price, item_id))
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")
    conn.commit()
    conn.close()
    return {"message": "Updated in Database!"}

# ৪. DELETE (মুছে ফেলা) - লাল রঙ
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    conn = sqlite3.connect("items.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"message": "Deleted from Database!"}
