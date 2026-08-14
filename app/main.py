from fastapi import FastAPI

from app.routes.user import router as user_router

app = FastAPI()

# connects it to the FastAPI application.
app.include_router(user_router)

# uvicorn app.main:app --reload
