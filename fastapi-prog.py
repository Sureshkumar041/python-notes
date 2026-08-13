from fastapi import Depends, FastAPI, status, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class PlayerDetail(BaseModel):
    id: int
    name: str
    age: int
    role: str


class PlayerListRes(BaseModel):
    message: str
    data: list[PlayerDetail]


class PlayerByIdRes(BaseModel):
    message: str
    data: PlayerDetail | None


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
    data: PlayerDetail


@app.post(
    "/players", response_model=CreatePlayerRes, status_code=status.HTTP_201_CREATED
)
def create_player(player: PlayerBM):
    new_id = max(p["id"] for p in players) + 1
    new_player = {**player.model_dump(), "id": new_id}
    players.append(new_player)
    return {"message": "Player created successfully", "data": new_player}


# 🏏 Next ball: HTTP status codes

players = [
    {"id": 1, "name": "suresh", "age": 25, "role": "All rounder"},
    {"id": 2, "name": "sk", "age": 26, "role": "Batter"},
    {"id": 3, "name": "kevin", "age": 33, "role": "Bowler"},
]

# response


@app.get("/players_list", response_model=PlayerListRes, status_code=status.HTTP_200_OK)
def get_players_list():
    return {"message": "Fetched player list successfully", "data": players}


@app.get(
    "/player_detail/{player_id}",
    response_model=PlayerByIdRes,
    status_code=status.HTTP_200_OK,
)
def get_player_detail(player_id: int):
    player_detail = next((p for p in players if p["id"] == player_id), None)

    if not player_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player detail with id {player_id} not found",
        )

    return {
        "message": "Fetched player detail successfully",
        "data": player_detail,
    }


class UpdatePlayerBM(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=18)
    role: str


class UpdatePlayerRes(BaseModel):
    message: str
    data: PlayerDetail


@app.put("/players/{player_id}", response_model=UpdatePlayerRes)
def update_players(player_id: int, payload: UpdatePlayerBM):
    player_detail = next((p for p in players if p["id"] == player_id), None)

    if not player_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player detail with id {player_id} not found",
        )

    # players[:] = [
    #     {**p, **payload.model_dump()} if p["id"] == player_id else p for p in players
    # ]

    player_detail.update(payload.model_dump())

    return {
        "message": "Updated player detail successfully",
        "data": player_detail,
    }


class DeletedPlayerRes(BaseModel):
    message: str


@app.delete(
    "/players/{player_id}",
    response_model=DeletedPlayerRes,
    status_code=status.HTTP_200_OK,
)
def delete_player(player_id: int):
    player_detail = next((p for p in players if p["id"] == player_id), None)

    if not player_detail:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Player detail with id {player_id} not found",
        )

    players[:] = [p for p in players if p["id"] != player_id]

    return {"message": "Deleted player successfully"}


# Lesson 11 — FastAPI Dependency Injection
print("\nLesson 11 — FastAPI Dependency Injection")


class CurrentPlayer(BaseModel):
    name: str
    role: str


class CurrentPlayerRes(BaseModel):
    message: str
    data: CurrentPlayer


class DashboardDetailRes(BaseModel):
    message: str
    data: CurrentPlayer


def get_current_player() -> CurrentPlayer:
    return {"name": "suresh", "role": "Batter"}


@app.get("/profile", response_model=CurrentPlayerRes)
def get_profile(data: CurrentPlayer = Depends(get_current_player)):
    return {"message": "Fetched player detail successfully", "data": data}


@app.get("/dashboard", response_model=DashboardDetailRes)
def get_dashboard(data: CurrentPlayer = Depends(get_current_player)):
    return {"message": "Fetched dashboard detail successfully", "data": data}


# 🎯 Dependency + Query Parameter
def player_role(role: str = "Batter"):
    return role


@app.get("/player-role")
def get_player_role(role: str = Depends(player_role)):
    return {"role": role}


# 🏏 Next ball: Reusable dependencies
print("\n🏏 Next ball: Reusable dependencies")

# dependency injection: write once, reuse everywhere.

# 🏏 Next level: Dependency with a class
print("\n🏏 Next level: Dependency with a class")


class PlayerDepBM(BaseModel):
    name: str
    role: str


class PlayerDepRes(BaseModel):
    message: str
    data: PlayerDepBM


class PlayerDependency:
    def __init__(self, name: str, role: str = "Batter"):
        self.name = name
        self.role = role

    def __call__(self) -> PlayerDepBM:
        return {"name": self.name, "role": self.role}


player_dependency = PlayerDependency("Shanmukh")


@app.get("/class-player", response_model=PlayerDepRes)
def get_class_player_dep(data: PlayerDepBM = Depends(player_dependency)):
    return {"message": "Fetched player dep successfully", "data": data}
