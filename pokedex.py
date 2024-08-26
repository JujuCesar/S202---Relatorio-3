from database import Database
from helper.writeAJson import  writeAJson
from main import db


class Pokedex:
    def __init__(self, database, collection):
        self.db = Database(database, collection)

    def query_by_type(self, poke_type): # Procurando por tipo
        result = self.db.collection.find({"type": poke_type})
        data = list(result)
        writeAJson(data, f"query_by_type")
        return data

    def query_by_height(self, min_height): # Procurando por altura
        result = self.db.collection.find({"height": {"$gte": min_height}}) # "gte" = greater than or equal
        data = list(result)
        writeAJson(data, f"query_by_height")
        return data

    def query_by_weaknesses(self, weaknesses): # Procurando por fraqueza
        result = self.db.collection.find({"weaknesses": weaknesses})
        data = list(result)
        writeAJson(data, f"query_by_weaknesses")
        return data

    def query_by_rarity(self, min_chance): # Procurando por raridade
        result = self.db.collection.find({"spawn_chance": {"$lte": min_chance}}) # "lte" = lesser than or equal
        data = list(result)
        writeAJson(data, f"query_by_rarity")
        return data

    def query_by_next_evolution(self, evolution_name): # Procurando por evolução específica
        result = self.db.collection.find({"next_evolution.name": evolution_name})
        data = list(result)
        writeAJson(data, f"query_by_next_evolution")
        return data


# Chamando as funções de query
if __name__ == "__main__":  # Váriável para executar o código
    pokedex = Pokedex(database="pokedex", collection="pokemons") # Instanciando a pokedex

    # Executando as querys criadas
    pokedex.query_by_type("Fire")
    pokedex.query_by_height("3.00 m")
    pokedex.query_by_weaknesses("Water")
    pokedex.query_by_rarity(0.2)
    pokedex.query_by_next_evolution("Charmeleon")