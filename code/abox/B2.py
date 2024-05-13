import pandas as pd
import random
from rdflib.namespace import RDF, RDFS, FOAF, XSD, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace
from rdflib import Literal

#importing csv files
authorsData = pd.read_csv('./data/authors.csv')
authorsPapersData = pd.read_csv('./data/authors_papers.csv')
conferencesData = pd.read_csv('data/conferences.csv')
conferencesData = pd.read_csv('data/conferences_editions.csv')
workshopsData = pd.read_csv('data/workshops.csv')
workshopsData = pd.read_csv('data/workshops_editions.csv')
journalsData= pd.read_csv('./data/journals.csv')
journalvolumesData = pd.read_csv('data/journal_volumes.csv')
papersData = pd.read_csv('data/papers.csv')
volumesData = pd.read_csv('data/volumes.csv')
affiliationsData = pd.read_csv('data/affiliations.csv')
companies_authorsData = pd.read_csv('data/companies_authors.csv')
universities_authorsData = pd.read_csv('data/universities_authors.csv')
universitiesData = pd.read_csv('data/universities.csv')
companiesData = pd.read_csv('data/companies.csv')


graph = Graph()

lab2 = Namespace("http://sdmlab2.org")

graph.bind('lab2', lab2)

#Author properties
#Author -- [name_author] --> String
graph.add((lab2.Author, lab2.name_author, XSD.string))
for x in range(len(authorsData[0])):
 graph.add((URIRef(lab2+authorsData[0][x]), lab2.name_author, Literal(authorsData[1][x])))

#Author -- [author] --> Paper

graph.add((lab2.Author, lab2.author, lab2.Paper))
for x in range(len(authorsPapersData[0])):
 graph.add((URIRef(lab2+authorsPapersData[0][x]), lab2.author, Literal(authorsPapersData[1][x])))
 graph.add((URIRef(lab2+authorsPapersData[0][x]), RDF.type, lab2.Author))

#Author -- [corresponding_author] --> Paper (subproperty of author)

#Author -- [:university] --> University
graph.add((lab2.Author, lab2.university, lab2.University))
for x in range(len(universities_authorsData[0])):
 graph.add((URIRef(lab2+universities_authorsData[1][x]), lab2.author, Literal(universities_authorsData[0][x])))
 graph.add((URIRef(lab2+universities_authorsData[1][x]), RDF.type, lab2.Author))

#Author -- [:company] --> Company
graph.add((lab2.Author, lab2.company, lab2.Company))
for x in range(len(companies_authorsData[0])):
 graph.add((URIRef(lab2+companies_authorsData[1][x]), lab2.company, Literal(universities_authorsData[0][x])))
 graph.add((URIRef(lab2+companies_authorsData[1][x]), RDF.type, lab2.Author))

#University properties
#University -- [name_university] --> String

graph.add((lab2.University, lab2.name_university, XSD.string))
for x in range(len(universitiesData[0])):
 graph.add((URIRef(lab2+universitiesData[0][x]), lab2.name_university, Literal(universitiesData[1][x])))

#Company properties
#Company -- [name_company] --> String
graph.add((lab2.Company, lab2.name_company, XSD.string))
for x in range(len(companiesData[0])):
 graph.add((URIRef(lab2+companiesData[0][x]), lab2.name_company, Literal(companiesData[1][x])))

#Review properties
#Review -- [content] --> String

#Review -- [decision] --> String

#Review -- [applied_to] --> Paper

#Review -- [created_by] --> Author