from utils import load_settings, save_settings
from neomodel import (config, StructuredRel, StructuredNode,  StringProperty, DateProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)
from bpmn_model import *

neo_connect_file = "neo4j_settings.json"

settings = load_settings(neo_connect_file)
config.DATABASE_URL = settings['neo4j']['database_url']

print(config.DATABASE_URL)
