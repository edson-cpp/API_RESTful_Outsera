import csv
from app.models import Movie

def parse_producers(producers_str: str):
    producers_str = producers_str.replace(" and ", ",")
    producers = producers_str.split(",")
    return [p.strip() for p in producers]

def load_movies(csv_path: str):
    movies = []

    with open(csv_path, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=";")

        for row in reader:
            movie = Movie(
                year=int(row["year"]),
                title=row["title"],
                studios=row["studios"],
                producers=parse_producers(row["producers"]),
                winner=row["winner"].strip().lower() == "yes"
            )

            movies.append(movie)

    return movies