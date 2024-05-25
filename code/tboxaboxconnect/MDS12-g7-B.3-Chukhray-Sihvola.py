
import pandas as pd
from rdflib.namespace import RDF, RDFS, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace

graph = Graph()

tboxpath = "C:\\Users\\Dima\\SDM_submission\\sdm-lab2\\code\\tbox\\tbox.ttl"
aboxpath = "C:\\Users\\Dima\\SDM_submission\\sdm-lab2\\code\\abox\\abox_nozeros.ttl"

graph.parse(tboxpath, format = 'ttl')
graph.parse(aboxpath, format = 'ttl')

print(len(graph))

file_path = "tbox_plus_abox.ttl"
graph.serialize(destination=file_path, format="ttl")
