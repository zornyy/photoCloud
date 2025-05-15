from typing import Union
from fastapi import FastAPI
from db.database import async_engine, Base
from api import users, photos

app = FastAPI()

@app.on_event("startup") # Code to execute on startup
async def startup():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("shutdown")
async def shutdown():
    # Close the database connection pool
    await async_engine.dispose()

@app.get("/health")
def healthcheck():
    return {"Message": "API running properly"}

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(photos.router, prefix="/photos", tags=["Photos"])

