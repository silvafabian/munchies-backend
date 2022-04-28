import requests
import os
from flask import Blueprint, jsonify, request

app_id = os.getenv('APP_ID')
app_key = os.getenv('APP_KEY')


homepage_api_url = f'https://api.edamam.com/api/recipes/v2?type=public&q=BEEF&app_id={app_id}&app_key={app_key}'

recipes = Blueprint('recipes', 'recipes')

@recipes.get('/')
def get_recipes():
  response = requests.get(homepage_api_url)
  res = response.json()
  # print(res)
  return jsonify(res)