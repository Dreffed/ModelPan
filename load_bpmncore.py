from utils import load_settings, save_settings, read_file
from neomodel import (config, StructuredRel, StructuredNode, StringProperty, IntegerProperty,
    UniqueIdProperty, UniqueProperty, RelationshipTo, RelationshipFrom, DoesNotExist)
from bpmn_model import BPMNTerm, TermRel

neo_connect_file = "neo4j_settings.json"

settings = load_settings(neo_connect_file)
config.DATABASE_URL = settings['neo4j']['database_url']

file_name = r'data/bpmnNames.csv'

rels = {}

for row in read_file(file_name):
    node_name = row['name']
    node_parent = row['Parent']

    if len(node_parent) > 0 :
        if not node_parent in rels:
            rels[node_parent] = []
        rels[node_parent].append(node_name)

    # get a node if it exists
    try:
        node = BPMNTerm.nodes.get(name=node_name)

    except DoesNotExist as e:
        try:
            BPMNTerm(name=node_name, descr=row['descr']).save()

        except UniqueProperty as e:
            print(e)

for node_label in rels:
    if len(rels[node_label]) > 0:
        print('\t{} -> {}'.format(node_label, len(rels[node_label])))

    try:
        node = BPMNTerm.nodes.get(name=node_label)
        for subnode_label in rels[node_label]:
            subnode = BPMNTerm.nodes.get(name=subnode_label)
            node.subterms.connect(subnode)

    except DoesNotExist as e:
        print(e)


    



