"""Module to invoke api"""
from mangum import Mangum
from fastapi import FastAPI
from app.api.api_v1.api import router as api_router

# add openapi_prefix="/dev" to fix docs in api getway
app = FastAPI(openapi_prefix="/dev")


@app.get("/")
async def root():
    """root endpoint"""
    return {"mesage": "Welcome to Cats API"}


app.include_router(api_router, prefix="/api/v1")
handler = Mangum(app)
