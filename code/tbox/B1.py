import os

from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal

graph = Graph()

lab2 = Namespace("http://sdmlab2.org/")

graph.bind('lab2', lab2)

#24 Classes

#University
graph.add((lab2.University, RDF.type, RDFS.Class))
graph.add((lab2.University, RDFS.label, Literal("University")))

#Company
graph.add((lab2.Company, RDF.type, RDFS.Class))
graph.add((lab2.Company, RDFS.label, Literal("Company")))

#Paper
graph.add((lab2.Paper, RDF.type, RDFS.Class))
graph.add((lab2.Paper, RDFS.label, Literal("Paper")))

#Journal
graph.add((lab2.Journal, RDF.type, RDFS.Class))
graph.add((lab2.Journal, RDFS.label, Literal("Journal")))

#Author
graph.add((lab2.Author, RDF.type, RDFS.Class))
graph.add((lab2.Author, RDFS.label, Literal("Author")))

#Volume
graph.add((lab2.Volume, RDF.type, RDFS.Class))
graph.add((lab2.Volume, RDFS.label, Literal("Volume")))

#Edition

graph.add((lab2.Edition, RDF.type, RDFS.Class))
graph.add((lab2.Edition, RDFS.label, Literal("Edition")))

#Review

graph.add((lab2.Review, RDF.type, RDFS.Class))
graph.add((lab2.Review, RDFS.label, Literal("Review")))

#Keyword
graph.add((lab2.Keyword, RDF.type, RDFS.Class))
graph.add((lab2.Keyword, RDFS.label, Literal("Keyword")))

#Name_Keyword
graph.add((lab2.Name_Keyword, RDF.type, RDFS.Class))
graph.add((lab2.Name_Keyword, RDFS.label, Literal("Name_Keyword")))

#Abstract
graph.add((lab2.Abstract, RDF.type, RDFS.Class))
graph.add((lab2.Abstract, RDFS.label, Literal("Abstract")))

#Title
graph.add((lab2.Title, RDF.type, RDFS.Class))
graph.add((lab2.Title, RDFS.label, Literal("Title")))

#Year
graph.add((lab2.Year, RDF.type, RDFS.Class))
graph.add((lab2.Year, RDFS.label, Literal("Year")))

#City_Conference
graph.add((lab2.City_Conference, RDF.type, RDFS.Class))
graph.add((lab2.City_Conference, RDFS.label, Literal("City_Conference")))

#Date_Conference
graph.add((lab2.Date_Conference, RDF.type, RDFS.Class))
graph.add((lab2.Date_Conference, RDFS.label, Literal("Date_Conference")))

#City_Workshop
graph.add((lab2.City_Workshop, RDF.type, RDFS.Class))
graph.add((lab2.City_Workshop, RDFS.label, Literal("City_Workshop")))

#Date_Workshop
graph.add((lab2.Date_Workshop, RDF.type, RDFS.Class))
graph.add((lab2.Date_Workshop, RDFS.label, Literal("Date_Workshop")))

#Date_Volume
graph.add((lab2.Date_Volume, RDF.type, RDFS.Class))
graph.add((lab2.Date_Volume, RDFS.label, Literal("Date_Volume")))

#Name_Journal
graph.add((lab2.Name_Journal, RDF.type, RDFS.Class))
graph.add((lab2.Name_Journal, RDFS.label, Literal("Name_Journal")))

#Content
graph.add((lab2.Content, RDF.type, RDFS.Class))
graph.add((lab2.Content, RDFS.label, Literal("Content")))

#Decision
graph.add((lab2.Decision, RDF.type, RDFS.Class))
graph.add((lab2.Decision, RDFS.label, Literal("Decision")))

#Name_Author
graph.add((lab2.Name_Author, RDF.type, RDFS.Class))
graph.add((lab2.Name_Author, RDFS.label, Literal("Name_Author")))

#Name_University
graph.add((lab2.Name_University, RDF.type, RDFS.Class))
graph.add((lab2.Name_University, RDFS.label, Literal("Name_University")))

#Name_Company
graph.add((lab2.Name_Company, RDF.type, RDFS.Class))
graph.add((lab2.Name_Company, RDFS.label, Literal("Name_Company")))

#Edges

#published_workshop
graph.add((lab2.published_workshop, RDF.type, RDF.Property))
graph.add((lab2.published_workshop, RDFS.domain, lab2.Paper))
graph.add((lab2.published_workshop, RDFS.range, lab2.Edition))
graph.add((lab2.published_workshop, RDFS.label, Literal("published_workshop")))

#published_conference
graph.add((lab2.published_conference, RDF.type, RDF.Property))
graph.add((lab2.published_conference, RDFS.domain, lab2.Paper))
graph.add((lab2.published_conference, RDFS.range, lab2.Edition))
graph.add((lab2.published_conference, RDFS.label, Literal("published_conference")))

#published_volume
graph.add((lab2.published_volume, RDF.type, RDF.Property))
graph.add((lab2.published_volume, RDFS.domain, lab2.Paper))
graph.add((lab2.published_volume, RDFS.range, lab2.Volume))
graph.add((lab2.published_volume, RDFS.label, Literal("published_volume")))

#name_author
graph.add((lab2.name_author, RDF.type, RDF.Property))
graph.add((lab2.name_author, RDFS.domain, lab2.Author))
graph.add((lab2.name_author, RDFS.range, lab2.Name_Author))
graph.add((lab2.name_author, RDFS.label, Literal("name_author")))

#name_university
graph.add((lab2.name_university, RDF.type, lab2.Property))
graph.add((lab2.name_university, RDFS.domain, lab2.University))
graph.add((lab2.name_university, RDFS.range, lab2.Name_University))
graph.add((lab2.name_university, RDFS.label, Literal("name_university")))

#university
graph.add((lab2.university, RDF.type, lab2.Property))
graph.add((lab2.university, RDFS.domain, lab2.Author))
graph.add((lab2.university, RDFS.range, lab2.University))
graph.add((lab2.university, RDFS.label, Literal("university")))

#company
graph.add((lab2.company, RDF.type, RDF.Property))
graph.add((lab2.company, RDFS.domain, lab2.Author))
graph.add((lab2.company, RDFS.range, lab2.Company))
graph.add((lab2.company, RDFS.label, Literal("company")))

#title
graph.add((lab2.title, RDF.type, RDF.Property))
graph.add((lab2.title, RDFS.domain, lab2.Paper))
graph.add((lab2.title, RDFS.range, lab2.Title))
graph.add((lab2.title, RDFS.label, Literal("title")))

#year
graph.add((lab2.year, RDF.type, RDF.Property))
graph.add((lab2.year, RDFS.domain, lab2.Paper))
graph.add((lab2.year, RDFS.range, lab2.Year))
graph.add((lab2.year, RDFS.label, Literal("year")))

#abstract
graph.add((lab2.abstract, RDF.type, RDF.Property))
graph.add((lab2.abstract, RDFS.domain, lab2.Paper))
graph.add((lab2.abstract, RDFS.range, lab2.Abstract))
graph.add((lab2.abstract, RDFS.label, Literal("abstract")))

#content
graph.add((lab2.content, RDF.type, RDF.Property))
graph.add((lab2.content, RDFS.domain, lab2.Review))
graph.add((lab2.content, RDFS.range, lab2.Content))
graph.add((lab2.content, RDFS.label, Literal("content")))

#decision
graph.add((lab2.decision, RDF.type, RDF.Property))
graph.add((lab2.decision, RDFS.domain, lab2.Review))
graph.add((lab2.decision, RDFS.range, lab2.Decision))
graph.add((lab2.decision, RDFS.label, Literal("decision")))

#name_keyword
graph.add((lab2.name_Keyword, RDF.type, RDF.Property))
graph.add((lab2.name_Keyword, RDFS.domain, lab2.Keyword))
graph.add((lab2.name_Keyword, RDFS.range, lab2.Name_Keyword))
graph.add((lab2.name_Keyword, RDFS.label, Literal("name_keyword")))

#name_journal
graph.add((lab2.name_journal, RDF.type, RDF.Property))
graph.add((lab2.name_journal, RDFS.domain, lab2.Journal))
graph.add((lab2.name_journal, RDFS.range, lab2.Name_Journal))
graph.add((lab2.name_journal, RDFS.label, Literal("name_journal")))

#journal
graph.add((lab2.journal, RDF.type, RDF.Property))
graph.add((lab2.journal, RDFS.domain, lab2.Volume))
graph.add((lab2.journal, RDFS.range, lab2.Journal))
graph.add((lab2.journal, RDFS.label, Literal("journal")))

#date_volume
graph.add((lab2.date_volume, RDF.type, RDF.Property))
graph.add((lab2.date_volume, RDFS.domain, lab2.Volume))
graph.add((lab2.date_volume, RDFS.range, lab2.Date_Volume))
graph.add((lab2.date_volume, RDFS.label, Literal("date_volume")))

#name_company
graph.add((lab2.name_company, RDF.type, RDF.Property))
graph.add((lab2.name_company, RDFS.domain, lab2.Company))
graph.add((lab2.name_company, RDFS.range, lab2.Name_Company))
graph.add((lab2.name_company, RDFS.label, Literal("name_company")))

#date_workshop
graph.add((lab2.date_workshop, RDF.type, RDF.Property))
graph.add((lab2.date_workshop, RDFS.domain, lab2.Edition))
graph.add((lab2.date_workshop, RDFS.range, lab2.Date_Workshop))
graph.add((lab2.date_workshop, RDFS.label, Literal("date_workshop")))

#city_workshop
graph.add((lab2.city_workshop, RDF.type, RDF.Property))
graph.add((lab2.city_workshop, RDFS.domain, lab2.Edition))
graph.add((lab2.city_workshop, RDFS.range, lab2.City_Workshop))
graph.add((lab2.city_workshop, RDFS.label, Literal("city_workshop")))

#date_conference
graph.add((lab2.date_conference, RDF.type, RDF.Property))
graph.add((lab2.date_conference, RDFS.domain, lab2.Edition))
graph.add((lab2.date_conference, RDFS.range, lab2.Date_Conference))
graph.add((lab2.date_conference, RDFS.label, Literal("date_conference")))

#city_conference
graph.add((lab2.city_conference, RDF.type, RDF.Property))
graph.add((lab2.city_conference, RDFS.domain, lab2.Edition))
graph.add((lab2.city_conference, RDFS.range, lab2.City_Conference))
graph.add((lab2.city_conference, RDFS.label, Literal("city_conference")))

#author
graph.add((lab2.author, RDF.type, RDF.Property))
graph.add((lab2.author, RDFS.domain, lab2.Author))
graph.add((lab2.author, RDFS.range, lab2.Paper))
graph.add((lab2.author, RDFS.label, Literal("author")))

#corresponding_author
graph.add((lab2.corresponding_author, RDF.type, RDF.Property))
graph.add((lab2.corresponding_author, RDFS.subPropertyOf, lab2.author))
graph.add((lab2.corresponding_author, RDFS.range, lab2.Paper))
graph.add((lab2.corresponding_author, RDFS.label, Literal("corresponding_author")))

#keyword
graph.add((lab2.keyword, RDF.type, RDF.Property))
graph.add((lab2.keyword,RDFS.domain, lab2.Paper))
graph.add((lab2.keyword, RDFS.range, lab2.Keyword))
graph.add((lab2.keyword, RDFS.label, Literal("keyword")))

#cites
graph.add((lab2.cites, RDF.type, RDF.Property))
graph.add((lab2.cites, RDFS.domain, lab2.Paper))
graph.add((lab2.cites, RDFS.range, lab2.Paper))
graph.add((lab2.cites, RDFS.label, Literal("cites")))

#created_by
graph.add((lab2.created_by, RDF.type, RDF.Property))
graph.add((lab2.created_by, RDFS.domain, lab2.Review))
graph.add((lab2.created_by, RDFS.range, lab2.Author))
graph.add((lab2.created_by, RDFS.label, Literal("created_by")))

#applied_to
graph.add((lab2.applied_to, RDF.type, RDF.Property))
graph.add((lab2.applied_to, RDFS.domain, lab2.Review))
graph.add((lab2.applied_to, RDFS.range, lab2.Paper))
graph.add((lab2.applied_to, RDFS.label, Literal("applied_to")))

#Literal properties

#conference
graph.add((lab2.conference, RDF.type, RDF.Property))
graph.add((lab2.conference, RDFS.domain, lab2.Edition))
graph.add((lab2.conference, RDFS.range, XSD.string))
graph.add((lab2.conference, RDFS.label, Literal("conference")))

#workshop
graph.add((lab2.workshop, RDF.type, RDF.Property))
graph.add((lab2.workshop, RDFS.domain, lab2.Edition))
graph.add((lab2.workshop, RDFS.range, XSD.string))
graph.add((lab2.workshop, RDFS.label, Literal("workshop")))


print(graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/tbox.ttl',format="ttl"))
