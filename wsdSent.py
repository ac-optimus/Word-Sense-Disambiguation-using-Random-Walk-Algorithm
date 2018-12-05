from nltk.corpus import wordnet as wn 
import networkx as nx
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from helperFUn import leskSim, edge_weight, graph, senseAssignment



G=graph("paper that is specially prepared for use in drafting")
#print (G.number_of_nodes())
#print(G.number_of_edges())
ranks = nx.pagerank(G,alpha=0.4)
tokenizer = RegexpTokenizer(r'\w+')
s1=tokenizer.tokenize("paper that is specially prepared for use in drafting")
dict1={}
for i in range(len(s1)):
    dict1[i] = [str(k) for k in wn.synsets(s1[i])]  #all the word senses of i th word here
    dict1[i] = [re.findall(r"'(.*?)'",o)[0] for o in dict1[i]]

senseLst = senseAssignment(dict1,ranks)
print (senseLst)
