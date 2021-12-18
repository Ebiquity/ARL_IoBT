import pandas as pd
import rdflib
from rdflib import Graph, RDF, RDFS, OWL, Namespace
import csv
#df = pd.read_csv('battlefield.csv')
from rdflib import Literal, XSD, BNode
graph1 = Graph()
graph1.parse('final23.ttl', format='ttl')
rquery = """
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
"""
results =graph1.query(rquery)

