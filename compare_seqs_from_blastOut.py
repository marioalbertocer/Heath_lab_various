import os,sys

path_report  = "/Users/marioceron/Desktop/blast/outputs/MAG141_MAG282_onlyChrom"
path_query = "/Users/marioceron/Desktop/blast/queries/onlyChr-Ref_282vs141.fas"

blast_report = map(lambda x: x.strip(), open(path_report, "r").readlines())

#parse_blast_report

for record in blast_report: print(record)

