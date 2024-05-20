
import pandas as pd
from rdflib.namespace import RDF, RDFS, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace

graph = Graph()

tboxpath = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/tbox2.ttl"
aboxpath = "/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/abox2_updated.ttl"

graph.parse(tboxpath, format = 'ttl')
graph.parse(aboxpath, format = 'ttl')

print(len(graph))

graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/combined2.ttl',format = 'ttl')
