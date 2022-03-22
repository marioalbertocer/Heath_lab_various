import os
from Bio import SeqIO
taxa = ["sm101", "sm114", "sm117B", "sm121", "sm123", "sm141", "sm142", "sm144A", "sm144B", "sm145", "sm146", "sm148B", "sm154", "sm157", "sm158B", "sm16", "sm169", "sm174", "sm176A", "sm176B", "sm177", "sm18", "sm182", "sm183", "sm184", "sm191", "sm192C", "sm192D", "sm194", "sm199", "sm200", "sm201", "sm204", "sm205", "sm206", "sm209", "sm21", "sm215", "sm216", "sm219", "sm220", "sm221", "sm225", "sm230", "sm231", "sm238", "sm24", "sm242", "sm243A", "sm243B", "sm245", "sm246", "sm247", "sm248", "sm258", "sm259", "sm25A", "sm261", "sm27", "sm276", "sm277", "sm278", "sm281", "sm282", "sm283", "sm286", "sm31", "sm313", "sm317", "sm318", "sm319", "sm32", "sm320", "sm322", "sm325", "sm33", "sm336", "sm34", "sm342", "sm358", "sm372", "sm373", "sm382", "sm384", "sm386", "sm39", "sm40", "sm406", "sm409", "sm41", "sm417", "sm42", "sm420", "sm421", "sm422", "sm43", "sm48", "sm498", "sm5", "sm508", "sm513", "sm514", "sm523", "sm524", "sm525", "sm526", "sm530", "sm533", "sm539", "sm540", "sm541", "sm57", "sm62", "sm65", "sm66", "sm67", "sm69", "sm701A", "sm701B", "sm710A", "sm710B", "sm714A", "sm714B", "sm72", "sm722A", "sm722B", "sm724A", "sm724B", "sm726A", "sm726B", "sm73", "sm733A", "sm739A", "sm740A", "sm746A", "sm746B", "sm748A", "sm748B", "sm749B", "sm749C", "sm753A", "sm753B", "sm755A", "sm755B", "sm757A", "sm757C", "sm758A", "sm761A", "sm762A", "sm79", "sm7A", "sm7B", "sm80", "sm82", "sm85", "sm86", "sm87", "sm88", "sm89", "sm9", "sm90A", "sm90B", "sm92", "sm93", "sm97", "sm14", "sm148A", "sm15", "sm158A", "sm17", "sm189", "sm25B", "sm26", "sm303", "sm335", "sm35", "sm36", "sm38", "sm46", "sm53", "sm54", "sm59", "sm6A", "sm6B", "sm71", "sm749A", "sm78", "sm8", "sm83", "sm84", "sm10"]
gfsPath = "/Users/marioceron/Downloads/melo/orthofinder_GFs/GFs_nucleotides/GFs_nucl_multiCopy_psmb/"
gfsPath2 = "/Users/marioceron/Downloads/melo/nucl_psmb_taxa/"

for taxon in taxa:
	f = open(gfsPath2 + taxon + ".fas", "w")	
	for gfFile in os.listdir(gfsPath):
		if gfFile.endswith(".fa"):
			for rec in SeqIO.parse(gfsPath + gfFile, "fasta"):
				taxonINgf = (rec.id).split("_")[0]
				gf = (rec.id).split("_")[1]	
				if taxon == taxonINgf:
					if gf in gfFile:
						f.write(">%s\n%s\n" % (rec.id, rec.seq))			
	print(taxon)