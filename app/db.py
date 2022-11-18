# imports
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from pydantic import BaseModel

engine = create_engine('sqlite:///database.db', echo=True)

meta = MetaData()
conn = engine.connect()


# classes van opperator
class Opperator(BaseModel):
    opp_id: int | None = -1
    opperator_name: str | None = "Invalid"
    primary_weapon: str | None = "Invalid"
    secondary_weapon: str | None = "Invalid"


# classes van players
class Player(BaseModel):
    player_id: int | None = -1
    user_name: str | None = "Invalid"
    first_name: str | None = "Invalid"
    last_name: str | None = "Invalid"
    email: str | None = "Invalid"
    mmr: int | None = 0


# De Opperators table
opperators = Table(
    'opperators', meta,
    Column('opp_id', Integer, primary_key=True),
    Column('opperator_name', String, unique=True),
    Column('primary_weapon', String),
    Column('secondary_weapon', String)
)

# De Players table
players = Table(
    'players', meta,
    Column('player_id', Integer, primary_key=True),
    Column('user_name', String, unique=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('email', String),
    Column('mmr', Integer)
)

# variablen van de player
player1 = {
    "player_id": 1,
    "user_name": "TBG_Benosboo",
    "first_name": "Dennis",
    "last_name": "Raaijmakers",
    "email": "test@test.com",
    "mmr": 3577
}

# variabelen van de opperators
opperator0 = {
    "opp_id": 0,
    "opperator_name": "Ela",
    "primary_weapon": "Scorpion EVO 3 A1",
    "secondary_weapon": "RG15"
}

opperator1 = {
    "opp_id": 1,
    "opperator_name": "Ash",
    "primary_weapon": "R4-C",
    "secondary_weapon": "M45 Meusoc"
}
opperator2 = {
    "opp_id": 2,
    "opperator_name": "Jäger",
    "primary_weapon": "416-C CARBINE",
    "secondary_weapon": "P12"
}
opperator3 = {
    "opp_id": 3,
    "opperator_name": "ace",
    "primary_weapon": "AK-12",
    "secondary_weapon": "P9"
}


# Functie om de database op te zetten
def setup_database():
    meta.create_all(engine)

    # basis opperators in de DB zetten
    insert_opperator(opperator0)
    insert_opperator(opperator1)
    insert_opperator(opperator2)
    insert_opperator(opperator3)

    # Basis player in de DB zetten
    insert_player(player1)


# Opperator inserten in de DB
def insert_opperator(opperator: dict):
    # Zorgen dat we geen dubble opperators doen
    if can_insert_opperator(opperator):
        # De opperator die toegevoegd wordt krijgt als waardes de opperator_name, primary_weapon en secondary_weapon mee
        insert_opp = opperators.insert().values(opperator_name=opperator.get("opperator_name"),
                                                primary_weapon=opperator.get("primary_weapon"),
                                                secondary_weapon=opperator.get("secondary_weapon"))
        # voert de query uit
        conn.execute(insert_opp)


# Insert een player in de DB
def insert_player(player: dict):
    # Zorgen dat we geen dubble usernames van players hebben
    if can_insert_player(player):
        # De player die toegevoegd wordt krijgt als waardes de user_name, first_name, last_name, email en mmr mee.
        ins = players.insert().values(player_id=player.get("player_id"), user_name=player.get("user_name"),
                                      first_name=player.get("first_name"), last_name=player.get("last_name"),
                                      email=player.get("email"), mmr=player.get("mmr"))
        # voert de query uit
        conn.execute(ins)


# Geeft een lijst van alle Opperators, opgevraagd uit de DB
def get_all_opperators():
    opps = opperators.select()

    query_resultaat = conn.execute(opps)
    opperator_lijst = []

    for row in query_resultaat:
        # row voorbeeld: 1,Ela,Scorpion EVO 3 A1,RG15
        opperator = {
            "opp_id": int(row[0]),  # 1
            "opperator_name": row[1],  # Ela
            "primary_weapon": row[2],  # Scorpion EVO 3 A1
            "secondary_weapon": row[3]  # RG15
        }
        opperator_lijst.append(opperator)
    return opperator_lijst


# Functie die een lijst met alle players van de database haalt
def get_all_players():
    all_players = players.select()
    query_resultaat = conn.execute(all_players)
    player_lijst = []

    for row in query_resultaat:
        player = {
            "player_id": int(row[0]),  # 1
            "user_name": row[1],  # TBG_Benosboo
            "first_name": row[2],  # Dennis
            "last_name": row[3],  # Raaijmakers
            "email": row[4],  # test@test.com
            "mmr": int(row[5])  # 3577
        }
        # De gegevens worden aan de lijst toegevoegd
        player_lijst.append(player)
    return player_lijst


# Kijkt of de opperator met een zelfde naam al bestaat
def can_insert_opperator(opperator: dict):
    for op in get_all_opperators():
        if op.get("opperatr_name") == opperator.get("opperator_name"):
            return False

    return True


# Kijkt of er een Player met dezelfde naam al bestaat
def can_insert_player(player: dict):
    for p in get_all_players():
        if p.get("user_name") == player.get("user_name"):
            return False

    return True
