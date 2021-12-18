#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import rdflib
from rdflib import Graph, RDF, RDFS, OWL, Namespace
import csv
#df = pd.read_csv('battlefield.csv')
from rdflib import Literal, XSD, BNode
graph1 = Graph()
graph1.parse('final23.ttl', format='ttl')
results = graph1.query("""
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX battlefield: <http://www.semanticweb.org/ebiquity/ontologies/2021/7/battlefield#>
PREFIX sosa: <http://www.w3.org/ns/sosa/phenomenonTime#>
PREFIX stix: <http://purl.org/cyber/stix/mitigates#>
SELECT   (?TS AS ?Time) (?BA As ?BandwidthStage)   ( ?code AS ?Mitigation_Program)  (?BA As ?Code_Parameter)  
WHERE {
?BA   rdf:type  battlefield:BandwidthAttack .
?BA battlefield:lowRange ?l .
?BA battlefield:highRange ?h .
?BO rdf:type  battlefield:BandwidthObservation .
?BO sosa:phenomenonTime  ?TS .
?BO battlefield:hasResult  ?Res .
?Res  battlefield:value ?val
FILTER ( ?val >=  ?l && ?val <=  ?h) .
?BAM stix:mitigates ?BA .
?BAM  battlefield:listedPlan ?MP .
?MP stix:hasProtectionProgram ?PP .
?PP battlefield:code ?code

}
ORDER BY ?TS
""")


final = []  
for row in results:
    a = row.Time[row.Time.find("#")+1:]
    b = row.BandwidthStage[row.BandwidthStage.find("#")+1:]
    c= row.Mitigation_Program          
    #d= row.Res[row.Res.find("#")+1:]
    data =[a,b,c]
    final.append(data)
            
    #print(a[a.find("#")+1:],",",b[b.find("#")+1:], row.Mitigation_Program,c[c.find("#")+1:])
    #print(row.Attack_Time, row.Detected_Attack, row.Mitigation_Program, row.Res

with open('output.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(final)

col_Names = ["Time","BandwidthStage", "Mitigation_Program"]
df = pd.read_csv('output.csv',names=col_Names)
print(df)


# In[ ]:




