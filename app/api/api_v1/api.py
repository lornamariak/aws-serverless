"""Module to route to get cats"""
from fastapi import APIRouter
from app.api.api_v1.endpoints import get_cats

router = APIRouter()
router.include_router(get_cats.router, prefix="/breeds", tags=["breeds"])
