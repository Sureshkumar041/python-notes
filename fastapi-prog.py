from fastapi import FastAPI, status
from pydantic import BaseModel, Field

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


# 🏏 Next ball — Request Body + Pydantic


class PlayerBM(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    role: str
    password: str = Field(min_length=6)


class PlayerResBM(BaseModel):
    name: str
    age: int
    role: str


# 🏏 Next ball: Response Models
class CreatePlayerRes(BaseModel):
    message: str
    data: PlayerResBM


@app.post(
    "/players", response_model=CreatePlayerRes, status_code=status.HTTP_201_CREATED
)
def create_player(player: PlayerBM):
    return {"message": "Player created successfully", "data": player.model_dump()}


# 🏏 Next ball: HTTP status codes
