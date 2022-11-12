from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

player = {
    "userName": "TBG_Benosboo",
    "firstName": "Dennis",
    "lastName": "Raaijmakers",
    "email": "test@test.com",
    "mmr": 3577
}

opperator0 = {
    "opp_id": 0,
    "opperatorName": "Ela",
    "primaryWeapon": "Scorpion EVO 3 A1",
    "secondaryWeapon": "RG15"
}
opperator1 = {
    "opp_id": 1,
    "opperatorName": "Ash",
    "primaryWeapon": "R4-C",
    "secondaryWeapon": "M45 Meusoc"
}
opperator2 = {
    "opp_id": 2,
    "opperatorName": "Jäger",
    "primaryWeapon": "416-C CARBINE",
    "secondaryWeapon": "P12"
}
opperator3 = {
    "opp_id": 3,
    "opperatorName": "ace",
    "primaryWeapon": "AK-12",
    "secondaryWeapon": "P9"
}

opperator_list = [opperator0, opperator1, opperator2, opperator3]


class Opperator(BaseModel):
    opp_id: int | None = -1
    opperatorName: str | None = "Invalid"
    primaryWeapon: str | None = "Invalid"
    secondaryWeapon: str | None = "Invalid"


class Player(BaseModel):
    userName: str | None = "Invalid"
    firstName: str | None = "Invalid"
    lastName: str | None = "Invalid"
    email: str | None = "Invalid"
    mmr: int | None = 0

#hiermee kan je een eigen player maken
@app.post("/player/", response_model=Player)
async def create_player(player: Player):
    return player

#hiermee vraag je de player op
@app.get("/player/", response_model=Player)
async def get_player():
    return player

#Laat de hele lijst van alle opperators zien
#Path parameter
@app.get("/opperator/info/all", response_model=list)
async def get_all():
    return opperator_list

#Hiermee kan je een specifieke opperator laten tonen door gebruik te maken van het id
#Query parameter
@app.get("/opperator/info/specific/{opp_id}", response_model=Opperator)
async def get_opperator(opp_id: int):
    for opp in opperator_list:
        if opp.get("opp_id") == opp_id:
            return opp

    return "Kies een lager ID nummer"
