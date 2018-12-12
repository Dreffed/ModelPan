from neomodel import (config, StructuredRel, StructuredNode,  StringProperty, DateProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)
    
class BPMNAssociation(StructuredRel):
    assc_type = StringProperty()
    data = DateProperty(default=None)

class BPMNContainer(StructuredNode):
    name = StringProperty(required=True)
    container_type = StringProperty(require=True)

    #

class BPMNProcess(StructuredNode):
    #fields
    name = StringProperty(required=True)
    process_type = StringProperty(required=True)

    # linkages
