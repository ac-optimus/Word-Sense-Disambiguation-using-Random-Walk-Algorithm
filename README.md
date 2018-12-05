
# Abstract
Disambiguating the sense from a word has always been an interesting task in NLP. 
Different ways to disambiguate includes :
1. Knowledge based Approaches 
      - Using some machine readable dictionaries like WordNet.
2. Using Machine Learning based Approaches
3. Hybrid Approached

This project aims to use one of the knowledge based WSD algorithms, i.e: **Random Walk Algorithm**



# Requirements
```
python           3.6.3
nltk             3.3
networkx         2.0
```

# Usage
```
Returns a list of senses corresponding to each of the ambiguous word in the given sentence.

python main.py sentence 
Note: sentence must be in quotes,eg: "this is a sentence"
```
> Note: some words cannot be disambiguated due to their absence in the wordnet.
# WordNet
[WordNet](https://en.wikipedia.org/wiki/WordNet) is a lexical database for the English language. It groups English words into 
sets of synonyms called synsets, provides short definitions and usage examples, and records a number of relations among these synonym sets or their members. WordNet can thus be seen as a combination of dictionary and thesaurus. While it is accessible to human users via a web browser, its primary use is in automatic text analysis and artificial intelligence applications. 

# The algorithm
To understand the algorithm lets take a sentence that has 4 words in it. The senses of the words are arranged in a graphical form. And then Pagerank algorithm is applied to find the most suitable word sense. In the graph (below) each node represents a sense and each edge represents the relation( similarity)between two senses. The edges are weighted using definition based semantic similarity(**lesk's method**).
For our example, the firt word, second word and third word have three senses each, while the forth word has only one sense
(list of senses are derived from wordnet). When the graph is made pagerank algorithm is used to rank all the nodes.
Then for each of the word the sense with the maximum pagerank score is selected as its sense.



![wsd](https://user-images.githubusercontent.com/26172160/49541076-ae51b100-f8f7-11e8-994c-05fff6c9cbd1.png)


## Lesk Method for the similarity of senses:
![lesk](https://user-images.githubusercontent.com/26172160/49543004-0b039a80-f8fd-11e8-85e7-2159e62ce568.png)
