from json import load, dump
from os import path

def load_settings(filename=r"settings.json"):
    if not path.exists(filename):
        settings = {
            'neo4j': {
                'database_url':r'bolt://neo4j:test@localhost:7687'
            }
        }
        save_settings(settings, filename)
        return settings
        
    # Load credentials from json file
    with open(filename, "r") as file:  
        settings = load(file)
    return settings

def save_settings(settings = {}, filename=r"settings.json"):


    # Save the credentials object to file
    with open(filename, "w") as file:  
        dump(settings, file)    