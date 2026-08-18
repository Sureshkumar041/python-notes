from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.user import router as user_router
from app.routes.file import router as file_router

app = FastAPI()
# uvicorn app.main:app --reload

# connects it to the FastAPI application.
app.include_router(user_router)
app.include_router(file_router)

# 
app.mount("/uploads", StaticFiles(directory="storage"), name="uploads")
