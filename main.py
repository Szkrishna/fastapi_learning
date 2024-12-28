from fastapi import FastAPI, HTTPException
from schemas import GenreURLChoices, BandBase, BandCreate, BandWithID

app = FastAPI()

BANDS = [
    {"id": 1, "name": "The Beatles", "genre": "Rock"},
    {"id": 2, "name": "Queen", "genre": "Rock"},
    {"id": 3, "name": "Pink Floyd", "genre": "Progressive Rock", "albums": [{
            "title": 'Mater of Reality', "release_date": '1971-11-11' 
        }
    ]},
    {"id": 4, "name": "Led Zeppelin", "genre": "Hard Rock"},
    {"id": 5, "name": "The Rolling Stones", "genre": "Rock"},
    {"id": 6, "name": "Nirvana", "genre": "Grunge", "albums": [{
            "title": 'Mater of Reality', "release_date": '1971-11-11' 
        }
    ]},
]

@app.get("/")
async def start():
    return "Application Started"


@app.get("/bands")
async def bands(genre: GenreURLChoices | None = None, has_album: bool = False) -> list[BandBase]:
    band_list = [BandBase(**b) for b in BANDS]
    if genre:
        band_list = [
            b for b in band_list if b.genre.lower() == genre.value
        ]
    if has_album:
        band_list = [b for b in band_list if len(b.albums) > 0]
    else:
        return band_list


@app.get("/bands/{band_id}")
async def band(band_id: int) -> BandBase:
    band = next((BandBase(**b) for b in BANDS if b['id'] == band_id), None)
    if band is None:
        raise HTTPException(status_code=404, detail="Not Found")
    return band


@app.get("/bands/genre/{genre}")
async def get_band_by_genre(genre: str):
    return [
        b for b in BANDS if b['genre'].lower() == genre.lower()
    ]

@app.post('/bands')
async def create_band(band_data: BandCreate) -> BandWithID:
    id = BANDS[-1]['id'] + 1
    band = BandWithID(id=id, **band_data.model_dump()).model_dump()
    BANDS.append(band)
    return band