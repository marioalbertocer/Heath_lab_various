import os, sys
from Bio import GenBank
from Bio import SeqIO

def get_parameters(arguments):
	parameters = []
	parameters = list(map(lambda x: x.strip(), arguments))
	help_message = """
		correct use... python3 seqFROMgbk.py path2gbkfiles ids_list path2out
		path2gbkfiles: the path to your genbank(annotation) files
		ids_list: a list of sequences that you want to extract. For EVERYTHING put -all
		path2out: the path where you want your output
		"""
	return(parameters, help_message)
	
def make_dirs(out_path):
	paths = [out_path + "/out/", out_path + "/out/nuc/", out_path + "/out/prot/", out_path + "/out/nam/"]
	for p in paths: 
		if not os.path.exists(p): os.system("mkdir " + p)
	return(paths)
	
def main():
	parameters = (get_parameters(sys.argv[1:]))
	if len(parameters[0]) != 3:
		print(parameters[1])
		exit()
	else:
		genomes_path, list_ids, out_path = parameters[0]
		ids = list(map(lambda x: x.strip(), open(list_ids, "r").readlines()))
		dir_out, dir_outNuc, dir_outPro, dir_outNam = make_dirs(out_path)
		
		for genome_file in os.listdir(genomes_path):
			if genome_file.endswith(".gbk"):
				strain = genome_file.replace(".gbk", "")
				idsXstrain = list(filter(lambda score: score.startswith(strain + ","), ids))
				out_nuc = open(dir_outNuc + strain + ".fasta", "w")
				out_pro = open(dir_outPro + strain + ".fasta", "w")
				idf = open(dir_outNam + strain + ".txt", "w")
				coun = 0
				
				for rec in SeqIO.parse(genomes_path + "/" + genome_file, "genbank"):
					for id_s in idsXstrain:
						id_only = id_s.split(",")[1].strip()
						if rec.id == id_only:
							for feat in rec.features:
								if feat.type == "CDS":
									prod_name = str(feat.qualifiers['product'][0])
									prot_seq = str(feat.qualifiers['translation'][0])
									nucl_seq = str(feat.extract(rec).seq)
									print("%s,%s,%s" % (coun, id_s, prod_name))
									idf.write("%s,%s,%s\n" % (coun, id_only, prod_name))
									out_nuc.write(">%s_%s_%s\n%s\n" % (strain, coun, id_only, nucl_seq))
									out_pro.write(">%s_%s_%s\n%s\n" % (strain, coun, id_only, prot_seq))
									coun += 1
									
if __name__ == "__main__":
	main()