"""Module to get a list of cat breeds"""
import uuid
import requests
import boto3
from fastapi import APIRouter, HTTPException

router = APIRouter()
s3 = boto3.client("s3")
BUCKET_NAME = "catsapi"

def get_breeds():
    """get all the breeds available"""
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, timeout=20)
    if response.status_code == 200:
        breeds = response.json()
        breed_dict = {breed["id"]: breed["name"] for breed in breeds}
        return breed_dict
    return None

def get_cat_type(breed_name):
    """get the details of a specific cat breed"""
    cat_breeds = get_breeds()
    breed_id = None
    for key, value in cat_breeds.items():
        if value == breed_name:
            breed_id = key
            break
    if breed_id is None:
        return "Breed not found"
    url = f"https://api.thecatapi.com/v1/breeds/search?q={breed_id}"
    response = requests.get(url, timeout=20)
    if response.status_code == 200 and len(response.json()) > 0:
        return response.json()[0]
    return None

@router.get("/")
def list_breeds():
    """Endpoint to retrieve all cat breeds"""
    breeds = get_breeds()
    if breeds:
        return breeds
    raise HTTPException(status_code=500, detail="Failed to retrieve cat breeds")

@router.get("/{breed_name}")
def get_breed_details(breed_name: str):
    """Endpoint to retrieve details of a specific cat breed"""
    breed = get_cat_type(breed_name)
    if breed:
        # Write the breed details to S3
        object_id = str(uuid.uuid4())
        csv_data = ",".join([str(val) for val in breed.values()])
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=f"{object_id}.csv",
            Body=csv_data.encode("utf-8")
        )
        return breed
    raise HTTPException(status_code=404, detail="Breed not found")
    