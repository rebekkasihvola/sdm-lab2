import pandas as pd
from rdflib.namespace import RDF, RDFS, FOAF, XSD, URIRef
from rdflib import Graph
import pandas as pd
from rdflib import Namespace
from rdflib import Literal

from urllib.parse import quote

#importing csv files
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


lab2 = Namespace("http://sdmlab2.org/")

graph.bind('lab2', lab2)

graph.add((lab2.Author, lab2.name_author, lab2.Name_Author))
for i in range(len(authorsData)):
    row = authorsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), lab2.name_author, URIRef(lab2 + row.iloc[1])])

#Author -- [author] --> Paper

graph.add((lab2.Author, lab2.author, lab2.Paper))
for i in range(len(authorsPapersData)):
    row = authorsPapersData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), lab2.author, URIRef(lab2 + row.iloc[1])])


#Author -- [corresponding_author] --> Paper (subproperty of author)
graph.add((lab2.Author, lab2.corresponding_author, lab2.Paper))
for i in range(len(mainauthorsData)):
    row = mainauthorsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), lab2.corresponding_author, URIRef(lab2 + row.iloc[1])])

#Author -- [university] --> University
graph.add((lab2.Author, lab2.university, lab2.University))
for x in range(len(universities_authorsData)):
 row = universities_authorsData.iloc[x]
 graph.add((URIRef(lab2+str(row.iloc[1])), lab2.university, URIRef(lab2+row[0])))
 

# Author -- [company] --> Company
graph.add((lab2.Author, lab2.company, lab2.Company))
for i in range(len(companies_authorsData)):
    row = companies_authorsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.company, URIRef(lab2 + row.iloc[0])))

# University properties
# University -- [name_university] --> Name_University
graph.add((lab2.University, lab2.name_university, lab2.Name_University))
for i in range(len(universitiesData)):
    row = universitiesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_university, URIRef(lab2 + row.iloc[1])))

# Company properties
# Company -- [name_company] --> Name_Company
graph.add((lab2.Company, lab2.name_company, lab2.Name_Company))
for i in range(len(companiesData)):
    row = companiesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_company, URIRef(lab2 + row.iloc[1])))

# Review properties
# Review -- [content] --> Content
graph.add((lab2.Review, lab2.content, lab2.Content))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.content, URIRef(quote(lab2 + row.iloc[3]))))

# Review -- [decision] --> Decision
graph.add((lab2.Review, lab2.decision, lab2.Decision))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.decision, URIRef(lab2 + row.iloc[4])))

# Review -- [applied_to] --> Paper
graph.add((lab2.Review, lab2.applied_to, lab2.Paper))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.applied_to, URIRef(lab2 + row.iloc[2])))

# Review -- [created_by] --> Author
graph.add((lab2.Review, lab2.created_by, lab2.Author))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.created_by, URIRef(lab2 + str(row.iloc[1]))))

# Paper properties
# Paper -- [title] --> Title
graph.add((lab2.Paper, lab2.title, lab2.Title))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.title, URIRef(lab2 + row.iloc[1])))

# Paper -- [year] --> Year
graph.add((lab2.Paper, lab2.year, lab2.Year))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.year, URIRef(lab2 + str(row.iloc[3]))))

# Paper -- [abstract] --> Abstract
graph.add((lab2.Paper, lab2.abstract, lab2.Abstract))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.abstract, URIRef(lab2 + str(row.iloc[2]))))

# Paper -- [cites] --> Paper
graph.add((lab2.Paper, lab2.cites, lab2.Paper))
for i in range(len(citationsData)):
    row = citationsData.iloc[i]
    graph.add([URIRef(lab2 + str(row.iloc[0])), lab2.cites, URIRef(lab2 + row.iloc[1])])

# Paper --[published_volume] --> Volume
graph.add((lab2.Paper, lab2.published_volume, lab2.Volume))
for i in range(len(volumesPapersData)):
    row = volumesPapersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.published_volume, URIRef(lab2 + row.iloc[0])))

# Paper --[published_conference] --> Edition
graph.add((lab2.Paper, lab2.published_conference, lab2.Edition))
for i in range(len(conferencesEditionsPapersData)):
    row = conferencesEditionsPapersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.published_conference, URIRef(lab2 + row.iloc[0])))

# Paper --[published_workshop] --> Edition
graph.add((lab2.Paper, lab2.published_workshop, lab2.Edition))
for i in range(len(workshopsEditionsPapersData)):
    row = workshopsEditionsPapersData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.published_conference, URIRef(lab2 + row.iloc[0])))

# Paper --[keyword] --> Keyword
graph.add((lab2.Paper, lab2.keyword, lab2.Keyword))
for i in range(len(keywordPaperData)):
    row = keywordPaperData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.keyword, URIRef(lab2 + row.iloc[0])))

# Journal
# Journal -- [name_journal] --> Name_Journal
graph.add((lab2.Journal, lab2.name_journal, lab2.Name_journal))
for i in range(len(journalsData)):
    row = journalsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_journal, URIRef(lab2 + row.iloc[1])))

# Volume
# Volume -- [date_volume] --> Date_Volume
graph.add((lab2.Volume, lab2.date_volume, lab2.Date_Volume))
for i in range(len(volumesData)):
    row = volumesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_volume, URIRef(lab2 + row.iloc[2])))

# Volume -- [journal] --> Journal
graph.add((lab2.Volume, lab2.journal, lab2.Journal))
for i in range(len(journalvolumesData)):
    row = journalvolumesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[1])), lab2.journal, URIRef(lab2 + row.iloc[0])))

# Edition

# Edition -- [city_conference] --> City_Conference
graph.add((lab2.Edition, lab2.city_conference, lab2.City_Conference))
for i in range(len(conferencesData)):
    row = conferencesData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.city_conference, URIRef(lab2 + row.iloc[3])))

# Edition -- [date_conference] --> Date_Conference
graph.add((lab2.Edition, lab2.date_conference, lab2.Date_Conference))
for i in range(len(conferencesEditionsData)):
    row = conferencesEditionsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_conference, URIRef(lab2 + row.iloc[2])))

# Edition -- [date_workshop] --> Date_Workshop
graph.add((lab2.Edition, lab2.date_workshop, lab2.Date_Workshop))
for i in range(len(workshopsEditionsData)):
    row = workshopsEditionsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.date_workshop, URIRef(lab2 + row.iloc[2])))

# Edition -- [city_workshop] --> City_Workshop
graph.add((lab2.Edition, lab2.city_workshop, lab2.City_Workshop))
for i in range(len(workshopsData)):
    row = workshopsData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.city_workshop, URIRef(lab2 + row.iloc[3])))

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
# Keyword -- [name_keyword] --> Name_Keyword
graph.add((lab2.Keyword, lab2.name_keyword, lab2.Name_Keyword))
for i in range(len(keywordData)):
    row = keywordData.iloc[i]
    graph.add((URIRef(lab2 + str(row.iloc[0])), lab2.name_keyword, URIRef(lab2 + row.iloc[1])))

graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/abox.ttl',format = 'ttl')
