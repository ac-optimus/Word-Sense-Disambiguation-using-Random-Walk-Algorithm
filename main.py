from nltk.corpus import wordnet as wn 
import networkx as nx
import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import RegexpTokenizer
from lesk import lesk
#pass defination1 and defination2 here


def edge_weight(g,sense,layer):
    #lets pass a one sense of a word and the trailing layer.
    #find the corresponding definations
    def1 = wn.synset(sense).definition()
    def2 = {}
    for i in range(len(layer)):
        
            def2[i] = wn.synset(layer[i]).definition()
            edge_weight = lesk(def1,def2[i])#pass two sense definitions
            g.add_edge(sense,layer[i],weight=edge_weight)
        #except:
        #    pass
        #dictionary of words versus their definition is ready
        



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
    rank = nx.pagerank(G,alpha=0.4)
    return rank

def senseAssignment(senseDict,Ranks):
    SenseLst=[]
    for word in senseDict:
        maxRank=0
        Sense=""
        for sense in senseDict[word]:
            if maxRank < Ranks[sense]:
                Sense = sense
        SenseLst.append(Sense)
    return SenseLst
        



if __name__ == "__main__":
    G=graph("paper that is specially prepared for use in drafting")
    print (G.number_of_nodes())
    print(G.number_of_edges())
    ranks = nx.pagerank(G,alpha=0.4)

    tokenizer = RegexpTokenizer(r'\w+')
    s1=tokenizer.tokenize("paper that is specially prepared for use in drafting")
    dict1={}
    
    for i in range(len(s1)):
        dict1[i] = [str(k) for k in wn.synsets(s1[i])]  #all the word senses of i th word here
        dict1[i] = [re.findall(r"'(.*?)'",o)[0] for o in dict1[i]]

    senseWord = senseAssignment(dict1,ranks)
    print (senseWord)

    