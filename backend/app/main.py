from database import Base
from database import engine

from models import User


from fastapi import FastAPI
from api import users

app = FastAPI(
    app.include_router(
    users.router
)

    title="LePan API",
    version="1.0.0"
)

Base.metadata.create_all(
    bind=engine
)


@app.get("/")
def root():

    return {
        "project": "LePan",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "health": "ok"
    }
