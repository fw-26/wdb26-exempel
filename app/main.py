from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.db import get_conn, create_schema

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Skapa databas-schema:
create_schema()

# tillfällig "databas"
temp_rooms = [
    { "room_number": 101, "room_type": "Double room", "price": 100},
    { "room_number": 202, "room_type": "Single room", "price": 80},
    { "room_number": 303, "room_type": "Suite", "price": 500}
]

@app.get("/")
def read_root():
    # testa databasen
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("""
            SELECT 
                'databasen funkar!' AS msg, 
                version() AS version
        """)
        db_status = cur.fetchone()
    return { "msg": "Välkommen till hotellets boknings-API", "db": db_status}

@app.get("/rooms")
def rooms():
    return temp_rooms

@app.post("/bookings")
def create_booking():
    # skapa bokningen i databasen, INSERT INTO bookings...
    return { "msg": "Bokning skapad!"}