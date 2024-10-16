import requests
from random import randint
from fastapi import FastAPI

app = FastAPI()

@app.get("/api/pokemon")
async def get_pokemon():
    variables = {
        "id": randint(1, 1025)
    }

    URL = "https://beta.pokeapi.co/graphql/v1beta"
    query = """
    query samplePokeAPIquery($id: Int!) {
      pokemon_v2_pokemon(where: {id: {_eq: $id}}) {
        name
        pokemon_v2_pokemonsprites {
          sprites(path: "front_default")
        }
      }
    }
    """
    response = requests.post(URL, json={"query": query, "variables": variables}).json()
    payload = {
        "name": response["data"]["pokemon_v2_pokemon"][0]["name"],
        "image": response["data"]["pokemon_v2_pokemon"][0]["pokemon_v2_pokemonsprites"][0]["sprites"]
    }
    return payload