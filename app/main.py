"""Module to invoke api"""
from mangum import Mangum
from fastapi import FastAPI
from app.api.api_v1.api import router as api_router

app = FastAPI()


@app.get("/")
async def root():
    """root endpoint"""
    return {"mesage": "hello cats"}

app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
