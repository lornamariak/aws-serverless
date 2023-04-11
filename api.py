"""Module to invoke api"""
from fastapi import FastAPI, HTTPException
from data import read_data

app = FastAPI()


@app.get("/breeds")
def list_breeds():
    """Endpoint to retrieve all cat breeds"""
    breeds = read_data.get_breeds()
    if breeds:
        return breeds
    else:
        raise HTTPException(status_code=500, detail="Failed to retrieve cat breeds")


@app.get("/breeds/{breed_name}")
def get_breed_details(breed_name: str):
    """Endpoint to retrieve details of a specific cat breed"""
    breed = read_data.get_cat_type(breed_name)
    if breed:
        return breed
    else:
        raise HTTPException(status_code=404, detail="Breed not found")
