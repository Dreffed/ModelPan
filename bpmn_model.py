from neomodel import (config, StructuredRel, StructuredNode,  StringProperty, DateProperty, IntegerProperty,
    UniqueIdProperty, RelationshipTo, RelationshipFrom)

class TermRel(StructuredRel):
    relType = StringProperty()

class BPMNAssociation(StructuredRel):
    assc_type = StringProperty()
    data = DateProperty(default=None)

class BPMNTerm(StructuredNode):
    name = StringProperty(unique_index=True, required=True)
    descr = StringProperty()

    subterms = RelationshipTo('BPMNTerm', 'CONTAINS', model=TermRel)

class BPMNContainer(StructuredNode):
    name = StringProperty(required=True)
    container_type = StringProperty(require=True)

class BPMNProcess(StructuredNode):
    #fields
    name = StringProperty(required=True)
    process_type = StringProperty(required=True)

    # linkages
