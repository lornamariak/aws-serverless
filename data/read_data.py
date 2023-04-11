"""Module to import data from via Cat API"""
import requests


def get_breeds():
    """get all the breeds available"""
    url = "https://api.thecatapi.com/v1/breeds"
    response = requests.get(url, timeout=20)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def get_cat_type(breed_name):
    """get the details of a specific cat breed"""
    url = f"https://api.thecatapi.com/v1/breeds/search?q={breed_name}"
    response = requests.get(url, timeout=20)
    if response.status_code == 200 and len(response.json()) > 0:
        return response.json()[0]
    else:
        return None
