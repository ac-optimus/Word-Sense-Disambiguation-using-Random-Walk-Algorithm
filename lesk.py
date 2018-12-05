#lesk without applying stemming or lemmentisation

def lesk(sense1,sense2):#takes two glosses as input
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
if __name__ == "__main__":
  #  s1 = input("enter the first sentence")
   # s2 = input("enter the sencond sentence")
    print (lesk("paper that is specially prepared for use in drafting","the art of transferring designs from specially prepared paper to a wood or glass or metal surface"))
    