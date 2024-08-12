from fastapi import FastAPI
from app.routes.note_routes import router as note_router

app = FastAPI()

app.include_router(note_router, prefix="/api", tags=["Notes"])


@app.get("/")
def read_root():
    return "Welcome to API"
