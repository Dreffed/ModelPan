from neomodel import (config, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)

config.DATABASE_URL = 'bolt://neo4j:password@localhost:7687'


class Container(StructuredNode):
    name = StringProperty(required=True)
    container_type = StringProperty(require=True)

    #

class BPMNProcess(StructuredNode):
    #fields
    name = StringProperty(required=True)
    process_type = StringProperty(required=True)

    # linkages
