import os,sys

f = open(sys.argv[1], "r").readlines()
n_taxa = sys.argv[2]
f = f[1:]
gf_count = {}

for line_report in f:
	line_report = line_report.strip()
	gf = line_report.split("\t")[0]
	rest = line_report.split("\t")[1:]
	c = 0
	for taxon in rest:
		if int(taxon) != 0:
			c += 1

	if int(c) == int(n_taxa):
		print(gf)
	
	
