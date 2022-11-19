import random

from . import db
from fastapi import FastAPI, Query, Path

from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
db.setup_database()
# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# hiermee kan je een eigen player maken
@app.post("/players/create", response_model=str)
async def create_player(p: dict):
    db.insert_player(p)
    return "Successfully created a new player"


# random opperators uit de lijst
# query parameter
@app.get("/opperators/info/query/random", response_model=list)
async def get_random_opperators(amount: int = Query(default=1, gt=0)):
    # een tijdelijke copy van de opperators, zodat we geen duplicates krijgen
    temp = db.get_all_opperators().copy()
    selected = []
    # Als het getal dat meegegeven wordt groter is of gelijk is aan de lengte van de lijst dan worden alle opperators getoont.
    if amount >= len(db.get_all_opperators()):
        return db.get_all_opperators()
    else:
        for i in range(amount):
            # variabelen voor een random getal tussen 0 en de lengte van de lijst.
            rand = random.randint(0, len(temp) - 1)
            rand_opp = temp[rand]
            # Voegen de geselecteerde random opperator aan de lijst
            selected.append(rand_opp)
            # We verwijderen de geselecteerde random opperator zodat we geen duplicates krijgen
            temp.remove(rand_opp)
    return selected


# hiermee vraag je de player op bij zijn naam
# path parameter

@app.get("/players/info/specific/{name}", response_model=db.Player)
async def get_player(name: str):
    for player in db.get_all_players():
        if player.get("first_name") == name:
            return player
    return db.Player()


# Laat alle players zien
@app.get("/players/info/all", response_model=list)
async def get_all_players():
    return db.get_all_players()


# Laat de hele lijst van alle opperators zien
@app.get("/opperators/info/all", response_model=list)
async def get_all():
    return db.get_all_opperators()


# Hiermee kan je een specifieke opperator laten tonen door gebruik te maken van het id
# path parameter

@app.get("/opperators/info/specific/{opp_id}", response_model=db.Opperator)
async def get_opperator(opp_id: int = Path(ge=0, le=60, default=1)):
    for opp in db.get_all_opperators():
        if opp.get("opp_id") == opp_id:
            return opp

    return db.Opperator()
