from nltk.corpus import wordnet as wn 
import networkx as nx
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer

def leskSim(sense1,sense2):#takes two glosses as input
    sent1 = sense1.split()  #aplly tokenization instead here
    sent2 = sense2.split()
    incmt1=0
    incmt2=0
    leskScr = 0
    count = 0
   # flag = 0 #this is see if last word was same or not
    while (incmt1<len(sent1)-1) :
        if incmt2 == len(sent2):#can shift this in the else
            #set it to zero
            incmt2 = 0
            incmt1 = incmt1 + 1
        
        if  sent1[incmt1] == sent2[incmt2] :
            #then start the itteration, dude
            
            count = count + 1
    #        flag = 1  #use count codition instead.
            
            incmt1 = incmt1 + 1
            incmt2 = incmt2 + 1
        
        else:
            
            if count>0:#the termination of last ngram found
                leskScr = leskScr + count**2
     #           flag = 0
                count = 0
                incmt2 = 0
            else:
                incmt2 = incmt2 + 1
    if count>0:
        leskScr = leskScr + count**2

    return leskScr

def edge_weight(g,sense,layer):
    #lets pass a one sense of a word and the trailing layer.
    #find the corresponding definations
    def1 = wn.synset(sense).definition()
    def2 = {}
    for i in range(len(layer)):
        
            def2[i] = wn.synset(layer[i]).definition()
            edge_weight = leskSim(def1,def2[i])#pass two sense definitions
            g.add_edge(sense,layer[i],weight=edge_weight)

def graph(sent1):#takes two sentence and generates wordsense graph
    G = nx.Graph()
    tokenizer = RegexpTokenizer(r'\w+')
    s1=tokenizer.tokenize(sent1)
    dict1={}
    
    for i in range(len(s1)):
        dict1[i] = [str(k) for k in wn.synsets(s1[i])]  #all the word senses of i th word here
        dict1[i] = [re.findall(r"'(.*?)'",o)[0] for o in dict1[i]]

 
    for i in dict1.keys():
        G.add_nodes_from(dict1[i])
        
    #here all the nodes are added
    #add the edges to it
    for l in dict1.keys():
        for senses in dict1[l]:
            if l<(len(dict1)-1):           
                edge_weight(G,senses,dict1[l+1])
    return G

def get_Ranks(Graph):
    rank = nx.pagerank(Graph,alpha=0.4)
    return rank

def senseAssignment(senseDict,Ranks):
    SenseLst=[]
    for word in senseDict:
        maxRank=0
        Sense=""
        for sense in senseDict[word]:
            if maxRank < Ranks[sense]:
                Sense = sense
        try:
            SenseLst.append(wn.synset(Sense).definition())
        except:
            SenseLst.append("NA")
    return SenseLst
        


