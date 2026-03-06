from fastapi import FastAPI
from app.service import calculate_intervals
from app.csv_loader import load_movies

app = FastAPI()
movies = []

@app.on_event("startup")
def startup_event():
    global movies
    movies = load_movies("data/movielist.csv")
    
@app.get("/")
def read_root():
    return {"status": "running"}

@app.get("/producers/intervals")
def get_intervals():
    return calculate_intervals(movies)