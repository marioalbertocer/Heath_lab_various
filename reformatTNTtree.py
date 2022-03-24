import os, sys
import dendropy

# This script takes two outputs from TNT, a tree with branch lengths and a tree with bootstrap values and
# and combines the information in just one tree that is compatible with figTree.
# use as ... python3 path_to_lengths_tree(nexus) path_to_bootstrap_tree(nexus) path_to_output(folder)

def getTrees(path2lenTree, path2bootTree):
	length_file = list(map(lambda x: x.strip(), open(path2lenTree, "r").readlines()))
	boot_file = list(map(lambda x: x.strip(), open(path2bootTree, "r").readlines()))
	lenTree = length_file[length_file.index("tree tagged_tree = [&U]") + 1] 
	booTree = boot_file[boot_file.index("tree tagged_tree = [&U]") + 1] 
	tree_object = dendropy.Tree.get_from_string(booTree, schema="newick")
	for nd in tree_object:
		if type(nd.label) is str:
			if "/" in nd.label:
				nd.label = ((nd.label).split("/")[1]).strip()
				if nd.label == "?" : nd.label = ""
	booTree_mod = (tree_object.as_string(schema="newick",)).strip()
	return lenTree, booTree_mod

def checkInt(character):
	try:
		int(character)
		return True
	except ValueError:
		return False
		
def takeNode(n_ind, tree):
	n_label = ""
	while checkInt(tree[n_ind]) is True or tree[n_ind] == ':':
		n_label += str(tree[n_ind])
		n_ind += 1
	return n_label

def main():
	lenTree, booTree_mod = getTrees(sys.argv[1], sys.argv[2])
	reftdTree = open(sys.argv[3] + "/tree_reformated.tree", "w") 
	while lenTree != booTree_mod:
		for i in range(0,len(lenTree)):
			if lenTree[i] != booTree_mod[i]:
				if lenTree[i] == ":":
					if checkInt(booTree_mod[i]) is False: 							
						n_label = takeNode(i, lenTree)
						booTree_mod = booTree_mod[:i] + n_label + booTree_mod[i:len(booTree_mod)]
					if checkInt(booTree_mod[i]) is True:
						n_label = takeNode(i, booTree_mod)
						lenTree = lenTree[:i] + n_label + lenTree[i:len(lenTree)]
				break	
	reftdTree.write("%s" % booTree_mod)
	print("%s\n\nReformatted tree saved as: %s/tree_reformated.tree" % (booTree_mod, sys.argv[3]))
if __name__ == "__main__":
	main()