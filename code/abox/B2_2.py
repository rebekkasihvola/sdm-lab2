import pandas as pd
import random
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
coauthorsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/coauthors.csv')
conferencesData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/Conferences_editions2.csv')
conferencesEditionsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferences_editions_data.csv')
conferencesEditionsPapersData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/conferencesEditions_papers.csv')
workshopsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/Workshops_editions2.csv')
workshopsEditionsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/Workshops_editions_data.csv')
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
reviewsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/modified_reviews_papers2.csv')
citationsData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/citations.csv')
keywordData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/keywords.csv')
keywordPaperData = pd.read_csv('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/keywords_papers.csv')


graph = Graph()

lab2 = Namespace("http://sdmlab2.org")

graph.bind('lab2', lab2)

#Author properties
#Author -- [name_author] --> String
graph.add((lab2.Author, lab2.name_author, XSD.string))
for i in range(len(authorsData)):
    row = authorsData.iloc[i]
    graph.add([URIRef(lab2 + "Author"+str(row.iloc[0])), lab2.name_author, Literal(row.iloc[1])])

#Author -- [corresponding_author] --> Paper (subproperty of author)
graph.add((lab2.Author, lab2.corresponding_author, lab2.Paper))
for i in range(len(mainauthorsData)):
    row = mainauthorsData.iloc[i]
    graph.add([URIRef(lab2 +"Author"+str(row.iloc[0])), lab2.corresponding_author, URIRef(lab2 +"Paper"+row.iloc[1])])

#Author -- [author] --> Paper 

graph.add((lab2.Author, lab2.author, lab2.Paper))
for i in range(len(coauthorsData)):
    row = coauthorsData.iloc[i]
    graph.add([URIRef(lab2 +"Author"+str(row.iloc[0])), lab2.author, URIRef(lab2 +"Paper"+row.iloc[1])])


#Author -- [university] --> University
graph.add((lab2.Author, lab2.university, lab2.University))
for x in range(len(universities_authorsData)):
 row = universities_authorsData.iloc[x]
 graph.add((URIRef(lab2+"Author"+str(row.iloc[1])), lab2.university, URIRef(lab2+"University"+row.iloc[0])))
 
# Author -- [company] --> Company
graph.add((lab2.Author, lab2.company, lab2.Company))
for i in range(len(companies_authorsData)):
    row = companies_authorsData.iloc[i]
    graph.add((URIRef(lab2 +"Author"+str(row.iloc[1])), lab2.company, URIRef(lab2 +"Company"+ row.iloc[0])))

#University properties
#University -- [name_university] --> String

graph.add((lab2.University, lab2.name_university, XSD.string))
for i in range(len(universitiesData)):
    row = universitiesData.iloc[i]
    graph.add((URIRef(lab2 +"University"+str(row.iloc[0])), lab2.name_university, Literal(row.iloc[1])))

#Company properties
#Company -- [name_company] --> String
graph.add((lab2.Company, lab2.name_company, XSD.string))
for i in range(len(companiesData)):
    row = companiesData.iloc[i]
    graph.add((URIRef(lab2 +"Company"+str(row.iloc[0])), lab2.name_company, Literal(row.iloc[1])))

#Review properties
#Review -- [content] --> String
graph.add((lab2.Review, lab2.content, XSD.string))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 +"Review"+str(row.iloc[0])), lab2.content, Literal(row.iloc[3])))

# Review -- [decision] --> String
graph.add((lab2.Review, lab2.decision, XSD.string))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 +"Review"+str(row.iloc[0])), lab2.decision, Literal(row.iloc[4])))

# Review -- [applied_to] --> Paper
graph.add((lab2.Review, lab2.applied_to, lab2.Paper))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + "Review"+str(row.iloc[0])), lab2.applied_to, URIRef(lab2 + "Paper"+str(row.iloc[2]))))

# Review -- [created_by] --> Author
graph.add((lab2.Review, lab2.created_by, lab2.Author))
for i in range(len(reviewsData)):
    row = reviewsData.iloc[i]
    graph.add((URIRef(lab2 + "Review"+str(row.iloc[0])), lab2.created_by, URIRef(lab2 +"Author"+ str(row.iloc[1]))))


# Paper properties
# Paper -- [title] --> String
graph.add((lab2.Paper, lab2.title, XSD.string))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[0])), lab2.title, Literal(row.iloc[1])))

# Paper -- [year] --> Int
graph.add((lab2.Paper, lab2.year, XSD.int))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[0])), lab2.year, Literal(row.iloc[3])))

# Paper -- [abstract] --> String
graph.add((lab2.Paper, lab2.abstract, XSD.string))
for i in range(len(papersData)):
    row = papersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[0])), lab2.abstract, Literal(str(row.iloc[2]))))

# Paper -- [cites] --> Paper
graph.add((lab2.Paper, lab2.cites, lab2.Paper))
for i in range(len(citationsData)):
    row = citationsData.iloc[i]
    graph.add([URIRef(lab2 + "Paper"+str(row.iloc[0])), lab2.cites, URIRef(lab2+"Paper" + str(row.iloc[1]))])

# Paper --[published_volume] --> Volume
graph.add((lab2.Paper, lab2.published_volume, lab2.Volume))
for i in range(len(volumesPapersData)):
    row = volumesPapersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[1])), lab2.published_volume, URIRef(lab2 +"Volume"+ str(row.iloc[0]))))

# Paper --[published_conference] --> Edition
graph.add((lab2.Paper, lab2.published_conference, lab2.Edition))
for i in range(len(conferencesEditionsPapersData)):
    row = conferencesEditionsPapersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[1])), lab2.published_conference, URIRef(lab2+"Edition" + row.iloc[0])))


# Paper --[published_workshop] --> Edition
graph.add((lab2.Paper, lab2.published_workshop, lab2.Edition))
for i in range(len(workshopsEditionsPapersData)):
    row = workshopsEditionsPapersData.iloc[i]
    graph.add((URIRef(lab2 + "Paper"+str(row.iloc[1])), lab2.published_workshop, URIRef(lab2 +"Edition"+ row.iloc[0])))

# Paper --[keyword] --> Keyword
graph.add((lab2.Paper, lab2.keyword, lab2.Keyword))
for i in range(len(keywordPaperData)):
    row = keywordPaperData.iloc[i]
    graph.add((URIRef(lab2 +"Paper"+ str(row.iloc[1])), lab2.keyword, URIRef(lab2 +"Keyword"+ row.iloc[0])))

# Journal
# Journal -- [name_journal] --> string
graph.add((lab2.Journal, lab2.name_journal, XSD.string))
for i in range(len(journalsData)):
    row = journalsData.iloc[i]
    graph.add((URIRef(lab2 + "Journal"+str(row.iloc[0])), lab2.name_journal, Literal(row.iloc[1])))

# Volume
# Volume -- [date_volume] --> date
graph.add((lab2.Volume, lab2.date_volume, XSD.date))
for i in range(len(volumesData)):
    row = volumesData.iloc[i]
    graph.add((URIRef(lab2 + "Volume"+str(row.iloc[0])), lab2.date_volume, Literal(row.iloc[2])))

# Volume -- [journal] --> Journal
graph.add((lab2.Volume, lab2.journal, lab2.Journal))
for i in range(len(journalvolumesData)):
    row = journalvolumesData.iloc[i]
    graph.add((URIRef(lab2 + "Volume"+str(row.iloc[1])), lab2.journal, URIRef(lab2+"Journal" + row.iloc[0])))

# Edition

# Edition -- [city_conference] --> string
graph.add((lab2.Edition, lab2.city_conference, XSD.string))
for i in range(len(conferencesData)):
    row = conferencesData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[1])), lab2.city_conference, Literal(row.iloc[3])))

# Edition -- [date_conference] --> Date
graph.add((lab2.Edition, lab2.date_conference, XSD.date))
for i in range(len(conferencesEditionsData)):
    row = conferencesEditionsData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[0])), lab2.date_conference,  Literal(row.iloc[2])))

#Create new data
# Edition -- [date_workshop] --> Date
graph.add((lab2.Edition, lab2.date_workshop, XSD.date))
for i in range(len(workshopsEditionsData)):
    row = workshopsEditionsData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[0])), lab2.date_workshop, Literal(row.iloc[2])))

# Edition -- [city_workshop] --> string
graph.add((lab2.Edition, lab2.city_workshop, XSD.string))
for i in range(len(workshopsData)):
    row = workshopsData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[1])), lab2.city_workshop, Literal(row.iloc[3])))

# Edition -- [workshop] --> String
graph.add((lab2.Edition, lab2.workshop, XSD.string))
for i in range(len(workshopsData)):
    row = workshopsData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[1])), lab2.workshop, Literal(row.iloc[2])))

# Edition -- [conference] --> String
graph.add((lab2.Edition, lab2.conference, XSD.string))
for i in range(len(conferencesData)):
    row = conferencesData.iloc[i]
    graph.add((URIRef(lab2 + "Edition"+str(row.iloc[1])), lab2.conference, Literal(row.iloc[2])))

# Keyword
# Keyword -- [name_keyword] --> string
graph.add((lab2.Keyword, lab2.name_keyword, XSD.string))
for i in range(len(keywordData)):
    row = keywordData.iloc[i]
    graph.add((URIRef(lab2 + "Keyword"+str(row.iloc[0])), lab2.name_keyword, Literal(row.iloc[1])))

graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/abox2.ttl',format = 'ttl')
