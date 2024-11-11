from typing import Union

from fastapi import FastAPI, HTTPException

app = FastAPI()

Bands = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Queen", "genre": "Rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "Progressive Rock"},
    {"id": 4, "name": "Led Zeppelin", "genre": "Hard Rock"},
    {"id": 5, "name": "The Rolling Stones", "genre": "Rock"},
    {"id": 6, "name": "Nirvana", "genre": "Grunge"},
]


@app.get("/bands")
def bands():
    return Bands


@app.get("/bands/{band_id}")
def band(band_id: int):
    band = next((b for b in Bands if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return band


@app.get("/bands/genre/{genre}")
def get_band_by_genre(genre: str):
    return [b for b in Bands if b['genre'].lower() == genre.lower()];

