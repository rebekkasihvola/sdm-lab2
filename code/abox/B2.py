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
conferencesEditionsData = pd.read_csv('data/conferences_editions.csv')
conferencesEditionsPapersData = pd.read_csv('data/conferencesEditions_papers.csv')
workshopsData = pd.read_csv('data/workshops.csv')
workshopsDataEditions = pd.read_csv('data/workshops_editions.csv')
workshopsEditionsPapersData = pd.read_csv('data/workshopsEditions_papers.csv')
journalsData= pd.read_csv('./data/journals.csv')
journalvolumesData = pd.read_csv('data/journal_volumes.csv')
papersData = pd.read_csv('data/papers.csv')
volumesData = pd.read_csv('data/volumes.csv')
volumesPapersData = pd.read_csv('data/volumes_papers.csv')
affiliationsData = pd.read_csv('data/affiliations.csv')
companies_authorsData = pd.read_csv('data/companies_authors.csv')
universities_authorsData = pd.read_csv('data/universities_authors.csv')
universitiesData = pd.read_csv('data/universities.csv')
companiesData = pd.read_csv('data/companies.csv')
reviewsData = pd.read_csv('data/reviews_papers.csv')
citationsData = pd.read_csv('data/citations.csv')
keywordData = pd.read_csv('data/keywords.csv')
keywordPaperData = pd.read_csv('data/keywords_papers.csv')

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
 graph.add((URIRef(lab2+authorsPapersData[0][x]), lab2.author,lab2+authorsPapersData[1][x]))


#Author -- [corresponding_author] --> Paper (subproperty of author)

#Author -- [:university] --> University
graph.add((lab2.Author, lab2.university, lab2.University))
for x in range(len(universities_authorsData[0])):
 graph.add((URIRef(lab2+universities_authorsData[1][x]), lab2.author, lab2+universities_authorsData[0][x]))
 

#Author -- [:company] --> Company
graph.add((lab2.Author, lab2.company, lab2.Company))
for x in range(len(companies_authorsData[0])):
 graph.add((URIRef(lab2+companies_authorsData[1][x]), lab2.company, lab2+companies_authorsData[0][x])))
 
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
graph.add((lab2.Review, lab2.content, XSD.string))
for x in range(len(reviewsData[0])):
 graph.add((URIRef(lab2+reviewsData[0][x]), lab2.content, Literal(reviewsData[3][x])))

#Review -- [decision] --> String
graph.add((lab2.Review, lab2.decision, XSD.string))
for x in range(len(reviewsData[0])):
 graph.add((URIRef(lab2+reviewsData[0][x]), lab2.decision, Literal(reviewsData[4][x])))

#Review -- [applied_to] --> Paper
graph.add((lab2.Review, lab2.applied_to, lab2.Paper))
for x in range(len(reviewsData[0])):
 graph.add((URIRef(lab2+reviewsData[0][x]), lab2.applied_to, lab2+reviewsData[2][x]))

#Review -- [created_by] --> Author
graph.add((lab2.Review, lab2.created_by, lab2.Author))
for x in range(len(reviewsData[0])):
 graph.add((URIRef(lab2+reviewsData[0][x]), lab2.created_by, lab2+reviewsData[1][x]))

#Paper properties
#Paper -- [title] --> String
graph.add((lab2.Paper, lab2.title, XSD.string))
for x in range(len(papersData[0])):
 graph.add((URIRef(lab2+papersData[0][x]), lab2.title, Literal(papersData[1][x])))

#Paper -- [year] --> int
graph.add((lab2.Paper, lab2.year, XSD.int))
for x in range(len(papersData[0])):
 graph.add((URIRef(lab2+papersData[0][x]), lab2.year, Literal(papersData[3][x])))
#Paper -- [abstract] --> String
graph.add((lab2.Paper, lab2.abstract, XSD.string))
for x in range(len(papersData[0])):
 graph.add((URIRef(lab2+papersData[0][x]), lab2.abstract, Literal(papersData[2][x])))
#Paper -- [cites] --> Paper
graph.add((lab2.Paper, lab2.cites, lab2.Paper))
for x in range(len(citationsData[0])):
 graph.add((URIRef(lab2+citationsData[0][x]), lab2.cites, lab2+citationsData[1][x]))

#Paper --[published_volume] --> Volume
graph.add((lab2.Paper, lab2.published_volume, lab2.Volume))
for x in range(len(volumesPapersData[0])):
 graph.add((URIRef(lab2+volumesPapersData[1][x]), lab2.published_volume, lab2+volumesPapersData[0][x]))

#Paper --[published_conference] --> Edition
graph.add((lab2.Paper, lab2.published_conference, lab2.Edition))
for x in range(len(conferencesEditionsPapersData[0])):
 graph.add((URIRef(lab2+conferencesEditionsPapersData[1][x]), lab2.published_conference, lab2+conferencesEditionsPapersData[0][x]))

#Paper --[published_workshop] --> Edition
graph.add((lab2.Paper, lab2.published_workshop, lab2.Edition))
for x in range(len(workshopsEditionsPapersData[0])):
 graph.add((URIRef(lab2+workshopsEditionsPapersData[1][x]), lab2.published_conference, lab2+workshopsEditionsPapersData[0][x]))

#Paper --[keyword] --> Keyword
graph.add((lab2.Paper, lab2.keyword, lab2.Keyword))
for x in range(len(keywordPaperData[0])):
 graph.add((URIRef(lab2+keywordPaperData[1][x]), lab2.keyword, lab2+keywordPaperData[0][x]))

#Journal
#Journal -- [name_journal] --> String
graph.add((lab2.Journal, lab2.name_journal, XSD.string))
for x in range(len(journalsData[0])):
 graph.add((URIRef(lab2+journalsData[0][x]), lab2.name_journal, Literal(journalsData[1][x])))

#Volume
#Volume -- [date_volume] --> Date
graph.add((lab2.Volume, lab2.date_volume, XSD.date))
for x in range(len(volumesData[0])):
 graph.add((URIRef(lab2+volumesData[0][x]), lab2.date_volume, Literal(volumesData[2][x])))

#Volume -- [journal] --> Journal
graph.add((lab2.Volume, lab2.journal, lab2.Journal))
for x in range(len(journalvolumesData[0])):
 graph.add((URIRef(lab2+journalvolumesData[1][x]), lab2.journal, lab2+journalvolumesData[0][x]))

#Edition
#Edition -- [conference] --> String
#Edition -- [city_Conference] --> String
#Edition -- [date_Conference] --> Date

#Keyword
#Keyword -- [name_keyword] --> String
graph.add((lab2.Keyword, lab2.name_keyword, XSD.string))
for x in range(len(keywordData[0])):
 graph.add((URIRef(lab2+keywordData[0][x]), lab2.name_keyword, Literal(keywordData[1][x])))
