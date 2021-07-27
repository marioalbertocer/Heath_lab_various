import os
from Bio import GenBank
from Bio import SeqIO

path2gbk = "/Users/marioceron/Downloads/genomas_completos/"
path2out = "/Users/marioceron/Downloads/Sinorhizobium_meliloti_strains_proteins/"

for gbk in os.listdir(path2gbk):
	if "gbk" in gbk:
		f = open(path2gbk + gbk, "r")
		n = open(path2out + gbk.replace("gbk", "fasta"), "w")
		for rec in SeqIO.parse(f, "genbank"):
			for feat in rec.features:
				if feat.type == "CDS":
					print(rec.name)
					print(feat.qualifiers['product'][0])
					print(feat.qualifiers['translation'][0])
					n.write(">%s_%s\n%s\n" % (rec.name, feat.qualifiers['product'][0], feat.qualifiers['translation'][0]))
		
