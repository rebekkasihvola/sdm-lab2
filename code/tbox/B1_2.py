from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal

graph = Graph()

lab2 = Namespace("http://sdmlab2.org")

graph.bind('lab2', lab2)

#9 Classes

#University
graph.add((lab2.University, RDF.type, RDFS.Class))
graph.add((lab2.University, RDFS.label, Literal("University")))

#Company
graph.add((lab2.Company, RDF.type, RDFS.Class))
graph.add((lab2.Company, RDFS.label, Literal("Company")))

#Journal
graph.add((lab2.Journal, RDF.type, RDFS.Class))
graph.add((lab2.Journal, RDFS.label, Literal("Journal")))

#Volume
graph.add((lab2.Volume, RDF.type, RDFS.Class))
graph.add((lab2.Volume, RDFS.label, Literal("Volume")))


#Paper
graph.add((lab2.Paper, RDF.type, RDFS.Class))
graph.add((lab2.Paper, RDFS.label, Literal("Paper")))


#Author
graph.add((lab2.Author, RDF.type, RDFS.Class))
graph.add((lab2.Author, RDFS.label, Literal("Author")))

#Edition
graph.add((lab2.Edition, RDF.type, RDFS.Class))
graph.add((lab2.Edition, RDFS.label, Literal("Edition")))

#Review
graph.add((lab2.Review, RDF.type, RDFS.Class))
graph.add((lab2.Review, RDFS.label, Literal("Review")))

#Keyword
graph.add((lab2.Keyword, RDF.type, RDFS.Class))
graph.add((lab2.Keyword, RDFS.label, Literal("Keyword")))

#Properties

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

#city_conference
graph.add((lab2.city_conference, RDF.type, RDF.Property))
graph.add((lab2.city_conference, RDFS.domain, lab2.Edition))
graph.add((lab2.city_conference, RDFS.range, XSD.string))
graph.add((lab2.city_conference, RDFS.label, Literal("city_conference")))
#date_conference
graph.add((lab2.date_conference, RDF.type, RDF.Property))
graph.add((lab2.date_conference, RDFS.domain, lab2.Edition))
graph.add((lab2.date_conference, RDFS.range, XSD.date))
graph.add((lab2.date_conference, RDFS.label, Literal("date_conference")))
#city_workshop
graph.add((lab2.city_workshop, RDF.type, RDF.Property))
graph.add((lab2.city_workshop, RDFS.domain, lab2.Edition))
graph.add((lab2.city_workshop, RDFS.range, XSD.string))
graph.add((lab2.city_workshop, RDFS.label, Literal("city_workshop")))
#date_workshop
graph.add((lab2.date_workshop, RDF.type, RDF.Property))
graph.add((lab2.date_workshop, RDFS.domain, lab2.Edition))
graph.add((lab2.date_workshop, RDFS.range, XSD.date))
graph.add((lab2.date_workshop, RDFS.label, Literal("date_workshop")))
#date_volume
graph.add((lab2.date_volume, RDF.type, RDF.Property))
graph.add((lab2.date_volume, RDFS.domain, lab2.Volume))
graph.add((lab2.date_volume, RDFS.range, XSD.date))
graph.add((lab2.date_volume, RDFS.label, Literal("date_volume")))
#name_author
graph.add((lab2.name_author, RDF.type, RDF.Property))
graph.add((lab2.name_author, RDFS.domain, lab2.Author))
graph.add((lab2.name_author, RDFS.range, XSD.string))
graph.add((lab2.name_author, RDFS.label, Literal("name_author")))

#name_university
graph.add((lab2.name_university, RDF.type, lab2.Property))
graph.add((lab2.name_university, RDFS.domain, lab2.University))
graph.add((lab2.name_university, RDFS.range, XSD.string))
graph.add((lab2.name_university, RDFS.label, Literal("name_university")))

#title
graph.add((lab2.title, RDF.type, RDF.Property))
graph.add((lab2.title, RDFS.domain, lab2.Paper))
graph.add((lab2.title, RDFS.range, XSD.string))
graph.add((lab2.title, RDFS.label, Literal("title")))

#year
graph.add((lab2.year, RDF.type, RDF.Property))
graph.add((lab2.year, RDFS.domain, lab2.Paper))
graph.add((lab2.year, RDFS.range, XSD.int))
graph.add((lab2.year, RDFS.label, Literal("year")))

#abstract
graph.add((lab2.abstract, RDF.type, RDF.Property))
graph.add((lab2.abstract, RDFS.domain, lab2.Paper))
graph.add((lab2.abstract, RDFS.range, XSD.string))
graph.add((lab2.abstract, RDFS.label, Literal("abstract")))

#applied_to
graph.add((lab2.applied_to, RDF.type, RDF.Property))
graph.add((lab2.applied_to, RDFS.domain, lab2.Review))
graph.add((lab2.applied_to, RDFS.range, lab2.Paper))
graph.add((lab2.applied_to, RDFS.label, Literal("applied_to")))

#content
graph.add((lab2.content, RDF.type, RDF.Property))
graph.add((lab2.content, RDFS.domain, lab2.Review))
graph.add((lab2.content, RDFS.range, XSD.string))
graph.add((lab2.content, RDFS.label, Literal("content")))

#decision
graph.add((lab2.decision, RDF.type, RDF.Property))
graph.add((lab2.decision, RDFS.domain, lab2.Review))
graph.add((lab2.decision, RDFS.range, XSD.string))
graph.add((lab2.decision, RDFS.label, Literal("decision")))


#name_Keyword
graph.add((lab2.name_keyword, RDF.type, RDF.Property))
graph.add((lab2.name_keyword, RDFS.domain, lab2.Keyword))
graph.add((lab2.name_keyword, RDFS.range, XSD.string))
graph.add((lab2.name_keyword, RDFS.label, Literal("name_keyword")))

#name_journal
graph.add((lab2.name_journal, RDF.type, RDF.Property))
graph.add((lab2.name_journal, RDFS.domain, lab2.Journal))
graph.add((lab2.name_journal, RDFS.range, XSD.string))
graph.add((lab2.name_journal, RDFS.label, Literal("name_journal")))

#name_company
graph.add((lab2.name_company, RDF.type, RDF.Property))
graph.add((lab2.name_company, RDFS.domain, lab2.Company))
graph.add((lab2.name_company, RDFS.range, XSD.string))
graph.add((lab2.name_company, RDFS.label, Literal("name_company")))

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

#Edges

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
graph.add((lab2.keyword, RDFS.domain, lab2.Paper))
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

#journal
graph.add((lab2.journal, RDF.type, RDF.Property))
graph.add((lab2.journal, RDFS.domain, lab2.Volume))
graph.add((lab2.journal, RDFS.range, lab2.Journal))
graph.add((lab2.journal, RDFS.label, Literal("journal")))

print(graph.serialize('/Users/rebekkasihvola/sdm-lab-2/sdm-lab2/data/tbox2.ttl',format="ttl"))