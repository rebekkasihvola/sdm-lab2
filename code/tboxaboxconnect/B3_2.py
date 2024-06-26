import pandas as pd
from rdflib.namespace import RDF, RDFS, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace


authorsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/authors.csv')
authorsPapersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/authors_papers.csv')
mainauthorsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/main_authors.csv')
conferencesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferences.csv')
conferencesEditionsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferences_editions_data.csv')
conferencesEditionsPapersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferencesEditions_papers.csv')
workshopsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops.csv')
workshopsEditionsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshops_editions_data.csv')
workshopsEditionsPapersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/workshopEditions_papers.csv')
journalsData= pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/journals.csv')
journalvolumesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/journals_volumes.csv')
papersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/papers.csv')
volumesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/volumes.csv')
volumesPapersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/volumes_papers.csv')
affiliationsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/affiliations.csv')
companies_authorsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/companies_authors.csv')
universities_authorsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/universities_authors.csv')
universitiesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/universities.csv')
companiesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/companies.csv')
reviewsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/reviews_papers.csv')
citationsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/citations.csv')
keywordData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/keywords.csv')
keywordPaperData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/keywords_papers.csv')


graph = Graph()

lab2 = Namespace("http://sdmlab2.org")

graph.bind('lab2', lab2)

""" #Author properties
#Author -- [name_author] --> String
graph.add((lab2.Author, lab2.name_author, XSD.string))
for i in range(len(authorsData)):
    row = authorsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), lab2.name_author, Literal(row.iloc[1])]) """

#Author -- [author] --> Paper make connection

for i in range(len(authorsPapersData)):
    row = authorsPapersData.iloc[i]
    #PaperID
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Paper])

#Author -- [corresponding_author] --> Paper (subproperty of author)

""" for i in range(len(mainauthorsData)):
    row = mainauthorsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), RDFS.subPropertyOf, lab2.Paper]) """


#Author -- [university] --> University

for x in range(len(universities_authorsData)):
 row = universities_authorsData.iloc[x]
 #UniversityID
 graph.add([URIRef(lab2+str(row.iloc[0])), RDF.type,lab2.University])
 
# Author -- [company] --> Company

for i in range(len(companies_authorsData)):
    row = companies_authorsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Company])

""" #University properties
#University -- [name_university] --> String

graph.add((lab2.University, lab2.name_university, XSD.string))
for i in range(len(universitiesData)):
    row = universitiesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_university, Literal(row.iloc[1])))

#Company properties
#Company -- [name_company] --> String
graph.add((lab2.Company, lab2.name_company, XSD.string))
for i in range(len(companiesData)):
    row = companiesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_company, Literal(row.iloc[1])))

#Review properties
#Review -- [content] --> String
graph.add((lab2.Review, lab2.content, XSD.string))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.content, Literal(row.iloc[3])))

# Review -- [decision] --> String
graph.add((lab2.Review, lab2.decision, XSD.string))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.decision, Literal(row.iloc[4]))) """

# Review -- [applied_to] --> Paper

for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    #PaperID
    graph.add([URIRef(lab2 + str(row.iloc[0])), RDF.type, lab2.Paper])

# Review -- [created_by] --> Author

for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    #AuthorID
    graph.add((URIRef(lab2 + str(row.iloc[0])), RDF.type, lab2.Author))

""" # Paper properties
# Paper -- [title] --> String
graph.add((lab2.Paper, lab2.title, XSD.string))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.title, Literal(row.iloc[1])))

# Paper -- [year] --> Int
graph.add((lab2.Paper, lab2.year, XSD.int))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.year, Literal(row.iloc[3])))

# Paper -- [abstract] --> String
graph.add((lab2.Paper, lab2.abstract, XSD.string))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.abstract, Literal(str(row.iloc[2])))) """

# Paper -- [cites] --> Paper

for i in range(len(citationsData)):
    row = citationsData.iloc[i]
    #Paperid
    graph.add([URIRef(lab2 + str(row.iloc[0])), RDF.type, lab2.Paper])

# Paper --[published_volume] --> Volume

for i in range(len(volumesPapersData)):
    row = volumesPapersData.iloc[i]
    #Volumeid
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Volume])

# Paper --[published_conference] --> Edition

for i in range(len(conferencesEditionsPapersData)):
    row = conferencesEditionsPapersData.iloc[i]
    #EditionID
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Edition])

# Paper --[published_workshop] --> Edition
graph.add((lab2.Paper, lab2.published_workshop, lab2.Edition))
for i in range(len(workshopsEditionsPapersData)):
    row = workshopsEditionsPapersData.iloc[i]
    #EditionID
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Edition])

# Paper --[keyword] --> Keyword
graph.add((lab2.Paper, lab2.keyword, lab2.Keyword))
for i in range(len(keywordPaperData)):
    row = keywordPaperData.iloc[i]
    #KeywordID
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Keyword])

""" # Journal
# Journal -- [name_journal] --> string
graph.add((lab2.Journal, lab2.name_journal, XSD.string))
for i in range(len(journalsData)):
    row = journalsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_journal, Literal(row.iloc[1])))

# Volume
# Volume -- [date_volume] --> date
graph.add((lab2.Volume, lab2.date_volume, XSD.date))
for i in range(len(volumesData)):
    row = volumesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_volume, Literal(row.iloc[2]))) """

# Volume -- [journal] --> Journal

for i in range(len(journalvolumesData)):
    row = journalvolumesData.iloc[i]
    #JournalID
    graph.add([URIRef(lab2 + str(row.iloc[1])), RDF.type, lab2.Journal])

# Edition

""" # Edition -- [city_conference] --> string
graph.add((lab2.Edition, lab2.city_conference, XSD.string))
for i in range(len(conferencesData)):
    row = conferencesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.city_conference, Literal(row.iloc[3])))

# Edition -- [date_conference] --> Date
graph.add((lab2.Edition, lab2.date_conference, XSD.date))
for i in range(len(conferencesEditionsData)):
    row = conferencesEditionsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_conference,  Literal(row.iloc[2])))

# Edition -- [date_workshop] --> Date
graph.add((lab2.Edition, lab2.date_workshop, XSD.date))
for i in range(len(workshopsEditionsData)):
    row = workshopsEditionsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_workshop, Literal(row.iloc[2])))

# Edition -- [city_workshop] --> string
graph.add((lab2.Edition, lab2.city_workshop, XSD.string))
for i in range(len(workshopsData)):
    row = workshopsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.city_workshop, Literal(row.iloc[3])))

# Edition -- [workshop] --> String
graph.add((lab2.Edition, lab2.workshop, XSD.string))
for i in range(len(workshopsData)):
    row = workshopsData.iloc[i]
    graph.add((URIRef(lab2 + row.iloc[0]), lab2.workshop, Literal(row.iloc[1])))

# Edition -- [conference] --> String
graph.add((lab2.Edition, lab2.conference, XSD.string))
for i in range(len(conferencesData)):
    row = conferencesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.conference, Literal(row.iloc[1])))

# Keyword
# Keyword -- [name_keyword] --> string
graph.add((lab2.Keyword, lab2.name_keyword, XSD.string))
for i in range(len(keywordData)):
    row = keywordData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_keyword, Literal(row.iloc[1])))
 """

graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/tbox_abox_connection.ttl',format = 'ttl')