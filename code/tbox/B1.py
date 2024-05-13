import Graph, Namespace, RDF, RDFS, XSD, Literal

graph = Graph()

lab2 = Namespace("http://sdmlab2.org")

graph.bind('lab2', lab2)

#University
graph.add((lab2.University, RDF.type, RDFS.Class))
graph.add((lab2.University, RDFS.label, Literal("University")))

#name_university

graph.add((lab2.name_university, RDFS.domain, lab2.University))
graph.add((lab2.name_university, RDFS.range, lab2.Name_University))
graph.add((lab2.name_university, RDFS.label, Literal("name_university")))

#Company
graph.add((lab2.Company, RDF.type, RDFS.Class))
graph.add((lab2.Company, RDFS.label, Literal("Company")))

#name_company
graph.add((lab2.name_company, RDF.type, RDF.Property))
graph.add((lab2.name_company, RDFS.domain, lab2.Company))
graph.add((lab2.name_company, RDFS.range, lab2.Name_Company))
graph.add((lab2.name_company, RDFS.label, Literal("name_company")))

#corresponding_author
graph.add((lab2.corresponding_author, RDF.type, RDF.Property))
graph.add((lab2.corresponding_author, RDFS.subProperty, RDF.author))
graph.add((lab2.corresponding_author, RDFS.label, Literal("corresponding_author")))

#author
graph.add((lab2.author, RDF.type, RDF.Property))
graph.add((lab2.author, RDFS.domain, lab2.Author))
graph.add((lab2.author, RDFS.range, lab2.Paper))
graph.add((lab2.author, RDFS.label, Literal("author")))

#name_author
graph.add((lab2.name_author, RDF.type, RDF.Property))
graph.add((lab2.name_author, RDFS.domain, lab2.Author))
graph.add((lab2.name_author, RDFS.range, lab2.Name_Author))
graph.add((lab2.name_author, RDFS.label, Literal("name_author")))

#Paper
graph.add((lab2.Paper, RDF.type, RDFS.Class))
graph.add((lab2.Paper, RDFS.label, Literal("Paper")))

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

#cited
graph.add((lab2.cited, RDF.type, RDF.Property))
graph.add((lab2.cited, RDFS.domain, lab2.Paper))
graph.add((lab2.cited, RDFS.range, lab2.Paper))
graph.add((lab2.cited, RDFS.label, Literal("cited")))

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

#tagged
graph.add((lab2.tagged, RDF.type, RDF.Property))
graph.add((lab2.tagged, RDFS.domain, lab2.Keyword))
graph.add((lab2.tagged, RDFS.range, lab2.Paper))
graph.add((lab2.tagged, RDFS.label, Literal("tagged")))

#name_Keyword
graph.add((lab2.name_Keyword, RDF.type, RDF.Property))
graph.add((lab2.name_Keyword, RDFS.domain, lab2.Keyword))
graph.add((lab2.name_Keyword, RDFS.range, lab2.Name_Keyword))
graph.add((lab2.name_Keyword, RDFS.label, Literal("name_Keyword")))

#Journal
graph.add((lab2.Journal, RDF.type, RDFS.Class))
graph.add((lab2.Journal, RDFS.label, Literal("Journal")))

#Volume
graph.add((lab2.Volume, RDF.type, RDFS.Class))
graph.add((lab2.Volume, RDFS.label, Literal("Volume")))

#Name_Journal
graph.add((lab2.name_journal, RDF.type, RDF.Property))
graph.add((lab2.name_journal, RDFS.domain, lab2.Journal))
graph.add((lab2.name_journal, RDFS.range, lab2.Name_Journal))
graph.add((lab2.name_journal, RDFS.label, Literal("name_journal")))

#name_Keyword
graph.add((lab2.name_Keyword, RDF.type, RDF.Property))

print(graph.serialize('data/tbox.ttl',format="ttl"))
