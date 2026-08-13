from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def entrance():
    return {"message": "Hey man!"}


@app.get("/play")
def play():
    return {"message": "Cricket ?"}


@app.get("/when")
def when():
    return {"message": "Sunday"}


@app.get("/team-members/{count}")
def team_member(count: int):
    return {"team_members_count": count}


@app.get("/players/{player_id}")
def get_player(player_id: int):
    return {"player_id": player_id, "message": "Player found"}


"""
GET /players/abc

will automatically produce a 422 validation error because abc isn't an integer. That's FastAPI + Pydantic working together. 🔥
"""


# 🏏 Next ball — Query Parameters
@app.get("/players")
def get_players(limit: int = 10):
    return {"limit": limit}


@app.get("/search_players")
def search_players(name: str, limit: int = 10):
    return {"name": name, "limit": limit}
