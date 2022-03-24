import os, sys
import dendropy

# This script takes two outputs from TNT, a tree with branch lengths and a tree with bootstrap values and
# and combines the information in just one tree that is compatible with figTree.
# use as ... python3 path_to_lengths_tree(nexus) path_to_bootstrap_tree(nexus) path_to_output(folder)

tree = '(smel101.fas:0.0000219829,((((((((((((((((((smel10.fas:0.0000716490,smel123.fas:0.0000680102)90.9/69:0.0000046782,(((((smel169.fas:0.0000829214,smel66.fas:0.0000570557)95.5/99:0.0000459437,smel79.fas:0.0000000740)100/99:0.0000480844,((((smel21.fas:0.0000521336,(((smel281.fas:0.0000629101,smel282.fas:0.0000401312)76.4/86:0.0000176547,smel283.fas:0.0000334038)100/91:0.0000714586,smel342.fas:0.0000729450)100/99:0.0000748118)100/86:0.0000195141,smel5.fas:0.0000542540)100/86:0.0000236329,smel259.fas:0.0000958644)100/86:0.0000389802,smel31.fas:0.0000777684)100/86:0.0000181933)100/86:0.0000270334,smel59.fas:0.0000920020)100/86:0.0000266762,smel336.fas:0.0000485959)100/86:0.0000354714)100/69:0.0000256137,smel242.fas:0.0000789754)100/87:0.0000500494,(((smel144A.fas:0.0000627529,smel144B.fas:0.0000519114)100/100:0.0000333322,((smel205.fas:0.0000585174,smel246.fas:0.0000651089)95.4/99:0.0000208153,((smel206.fas:0.0000356246,smel247.fas:0.0000379863)100/100:0.0000483664,smel248.fas:0.0000484428)100/100:0.0000321375)100/100:0.0001266825)100/100:0.0001914140,smel313.fas:0.0000877118)99.9/87:0.0000201180)100/100:0.0000884380,(((((((((smel158A.fas:0.0000200402,smel158B.fas:0.0000740767)100/100:0.0000450748,(((smel225.fas:0.0000984210,(((smel276.fas:0.0000292227,smel278.fas:0.0000802091)100/99:0.0000350092,smel382.fas:0.0000690058)100/86:0.0000389967,smel277.fas:0.0000179593)100/100:0.0000792628)100/86:0.0000290656,smel758A.fas:0.0000994851)99.4/85:0.0000201917,smel386.fas:0.0000741674)99.5/85:0.0000093858)100/85:0.0000364935,smel733A.fas:0.0000571039)100/85:0.0000247026,((smel540.fas:0.0000040894,smel541.fas:0.0000997882)100/100:0.0000855677,smel749C.fas:0.0000526589)100/86:0.0000113767)100/86:0.0000212606,(smel238.fas:0.0000538256,(smel243A.fas:0.0000835428,smel243B.fas:0.0000202673)100/83:0.0000278134)100/100:0.0000761565)100/99:0.0000499165,(smel261.fas:0.0000567791,smel762A.fas:0.0000714907)97.8/100:0.0000050250)100/83:0.0000328789,smel53.fas:0.0001010749)96.4/86:0.0000121488,(smel746A.fas:0.0000570150,smel746B.fas:0.0000688576)100/100:0.0000471286)100/100:0.0000960165,(smel192C.fas:0.0000291933,smel192D.fas:0.0001001097)100/100:0.0001795085)98.1/100:0.0000051745)100/100:0.0000409351,((smel146.fas:0.0000504905,smel755B.fas:0.0000764317)100/100:0.0000675687,(smel215.fas:0.0000364867,smel216.fas:0.0001170703)100/100:0.0000601884)100/100:0.0001181933)100/99:0.0000406987,(((((smel114.fas:0.0000377741,(smel117B.fas:0.0000537949,smel145.fas:0.0000769977)98.4/96:0.0000557048)100/100:0.0001055686,smel286.fas:0.0001387824)100/100:0.0000678936,(smel204.fas:0.0001722970,((((smel523.fas:0.0000316693,smel525.fas:0.0000209742)100/65:0.0000579471,smel73.fas:0.0000339814)100/96:0.0000994821,smel86.fas:0.0000123226)99.6/60:0.0000234640,smel526.fas:0.0000919443)100/100:0.0001031885)100/100:0.0000600008)100/100:0.0000400439,(((((((smel14.fas:0.0001240041,smel90A.fas:0.0000578490)100/99:0.0000351186,smel755A.fas:0.0000514238)100/100:0.0000602037,smel15.fas:0.0000768184)100/99:0.0000271160,((smel177.fas:0.0000144581,smel209.fas:0.0001039616)97.4/91:0.0000225533,smel90B.fas:0.0000387177)100/100:0.0000458865)94.2/73:0.0000036914,smel48.fas:0.0001061263)100/99:0.0000255558,(smel41.fas:0.0000534047,smel8.fas:0.0000495214)100/100:0.0000446129)100/100:0.0001075412,(((((smel154.fas:0.0000948604,smel174.fas:0.0000747516)100/100:0.0001064983,(((smel16.fas:0.0001066375,smel358.fas:0.0001333467)34.9/52:0.0000166438,(smel539.fas:0.0000817743,smel82.fas:0.0000683823)100/100:0.0000804517)100/100:0.0000616122,((smel184.fas:0.0001470469,smel54.fas:0.0000683517)100/100:0.0000525634,smel46.fas:0.0001007979)100/100:0.0000697942)100/100:0.0000145874)100/100:0.0000277438,((smel191.fas:0.0000721521,smel97.fas:0.0000443717)100/100:0.0000735141,((((smel245.fas:0.0000817529,smel748A.fas:0.0001274802)86.2/99:0.0000302396,smel749A.fas:0.0001048485)100/100:0.0000676509,smel406.fas:0.0001751831)100/100:0.0000363529,smel40.fas:0.0001156252)100/100:0.0000256027)100/100:0.0000552625)99.5/65:0.0000069631,(smel199.fas:0.0001252941,(smel25A.fas:0.0001066556,smel25B.fas:0.0000036881)100/100:0.0001012885)100/100:0.0000861987)73.9/34:0.0000034757,(((smel230.fas:0.0000342542,smel231.fas:0.0000465496)100/100:0.0000636179,smel9.fas:0.0000099569)100/100:0.0000375645,smel83.fas:0.0000400781)100/100:0.0001234561)95.8/88:0.0000162640)100/99:0.0000360733)98.7/73:0.0000059763,((((((smel182.fas:0.0000551554,smel43.fas:0.0001012806)54.1/98:0.0000519365,smel89.fas:0.0000942974)73.9/60:0.0000318115,smel84.fas:0.0000813953)100/84:0.0000459408,smel200.fas:0.0000190473)100/86:0.0000380133,smel24.fas:0.0000850165)94.4/61:0.0000091765,(smel6A.fas:0.0000275041,smel6B.fas:0.0000821326)100/100:0.0000764655)100/100:0.0001189501)100/89:0.0000299358)100/100:0.0000406232,(smel194.fas:0.0008764866,smel26.fas:0.0005552842)99.9/100:0.0001695045)100/100:0.0010310428,(((smel18.fas:0.0001612727,smel303.fas:0.0000987938)100/100:0.0005068541,(((smel220.fas:0.0000343519,(smel80.fas:0.0000610877,smel92.fas:0.0000443450)100/88:0.0000382558)99.8/88:0.0000200867,(smel32.fas:0.0000407479,smel93.fas:0.0000124576)100/100:0.0000390225)100/88:0.0000409563,smel710A.fas:0.0000545072)100/100:0.0030223807)100/100:0.0030186386,smel417.fas:0.0007568078)100/100:0.0013198565)100/100:0.0029688047,((smel17.fas:0.0000268416,((smel201.fas:0.0000488172,smel219.fas:0.0000217679)100/59:0.0000599968,((smel34.fas:0.0000596290,smel78.fas:0.0000234524)98.1/96:0.0000098178,(((smel42.fas:0.0000349828,smel87.fas:0.0000489125)100/62:0.0000164631,smel85.fas:0.0000069216)100/62:0.0000200742,smel88.fas:0.0000135144)100/100:0.0000514787)100/100:0.0000490330)98.3/71:0.0000288465)1.4/31:0.0000194951,(smel189.fas:0.0000632990,smel38.fas:0.0000544100)87.7/96:0.0000396947)100/100:0.0001725980)100/100:0.0029168326,(smel322.fas:0.0000922075,smel753B.fas:0.0000565855)100/100:0.0014798343)100/100:0.0017781842,(((((((smel121.fas:0.0000672085,smel757A.fas:0.0000384522)100/100:0.0000483581,(smel722A.fas:0.0000483323,smel757C.fas:0.0001069751)99.9/99:0.0000192184)100/99:0.0000448184,smel71.fas:0.0000466651)100/100:0.0010348413,((smel33.fas:0.0000991000,(smel57.fas:0.0000760643,smel65.fas:0.0000809921)100/100:0.0000784320)0/34:0.0000013253,smel35.fas:0.0001405874)100/100:0.0010254198)100/100:0.0006927854,((smel319.fas:0.0000919136,((smel335.fas:0.0000730982,smel409.fas:0.0000840780)100/100:0.0000384345,smel530.fas:0.0000618967)90.6/100:0.0000366887)100/100:0.0000364533,smel384.fas:0.0000608126)100/100:0.0011704859)100/100:0.0005767511,smel221.fas:0.0004643360)100/100:0.0018071843,(smel148A.fas:0.0000496976,smel148B.fas:0.0000987528)100/100:0.0008164547)100/100:0.0022866132)100/100:0.0026867017,((smel27.fas:0.0000918632,smel524.fas:0.0000498244)92/70:0.0000469982,smel36.fas:0.0000315306)100/100:0.0058516389)100/100:0.0095299564,(((((((smel141.fas:0.0000056958,smel67.fas:0.0000110069)99.5/100:0.0000048796,smel72.fas:0.0000114137)81.5/99:0.0000016539,(smel39.fas:0.0000174865,smel749B.fas:0.0000118215)0/91:0.0000000339)0/90:0.0000000840,(smel142.fas:0.0000093889,(smel7A.fas:0.0000016649,smel7B.fas:0.0000024283)100/100:0.0000110074)97/100:0.0000024114)99.9/100:0.0000061022,smel183.fas:0.0000272854)100/100:0.0000110789,(smel62.fas:0.0000196459,smel69.fas:0.0000147701)100/100:0.0000105864)100/100:0.0000103113,((smel325.fas:0.0000239257,smel739A.fas:0.0000269702)99.6/100:0.0000046504,smel761A.fas:0.0000251843)100/100:0.0000151415)100/100:0.0000231062)0/99:0.0000000882,((((smel157.fas:0.0000036794,smel748B.fas:0.0000016586)100/100:0.0000268857,(smel176A.fas:0.0000000339,smel176B.fas:0.0000008339)100/100:0.0000325785)100/100:0.0000283745,smel701B.fas:0.0000616290)95.6/100:0.0000024240,smel722B.fas:0.0000544240)100/100:0.0000131566)100/100:0.0000318994,smel726B.fas:0.0000520971)0/98:0.0000000842,((smel258.fas:0.0000572974,((((smel420.fas:0.0000000339,smel421.fas:0.0000000339)0/99:0.0000000852,smel498.fas:0.0000016363)31.5/96:0.0000012263,smel701A.fas:0.0000008212)0/94:0.0000000817,smel422.fas:0.0000004222)100/100:0.0000423731)85.8/100:0.0000007900,((((smel508.fas:0.0000040983,smel714A.fas:0.0000008437)100/100:0.0000166966,smel714B.fas:0.0000199423)100/100:0.0000209127,smel726A.fas:0.0000387003)86.8/100:0.0000007516,((smel513.fas:0.0000518598,smel514.fas:0.0000544256)35/99:0.0000008227,(smel533.fas:0.0000549700,(smel724A.fas:0.0000016524,smel724B.fas:0.0000015924)100/100:0.0000374790)96.7/100:0.0000025672)99.9/100:0.0000047713)88.5/100:0.0000008203)98.7/100:0.0000028524)98.5/100:0.0000032993,((smel372.fas:0.0000008444,smel373.fas:0.0000008440)100/100:0.0000236028,(smel740A.fas:0.0000111060,smel753A.fas:0.0000109048)100/100:0.0000163761)100/100:0.0000145433)100/100:0.0000090430,((smel317.fas:0.0000174871,smel710B.fas:0.0000187095)100/100:0.0000242208,(smel318.fas:0.0000002051,smel320.fas:0.0000026565)100/100:0.0000248340)92.1/100:0.0000014803);'
tree_object = dendropy.Tree.get_from_string(tree, schema="newick")
for nd in tree_object:
	if type(nd.label) is str:
		if "/" in nd.label:
			if sys.argv[1] == 'bt' : nd.label = ((nd.label).split("/")[1]).strip()
			if sys.argv[1] == 'sa' : nd.label = ((nd.label).split("/")[0]).strip()		
tree_mod = (tree_object.as_string(schema="newick",)).strip()			
print(tree_mod)