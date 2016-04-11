import numpy as np
import numexpr as ne

RANGE = 1+np.arange(1e6).astype(int) #Should be changed

def getL(num,RANGE):
    return ne.evaluate("num*RANGE").astype(str)

def getInsom(num,RANGE):
    #print "NUMBER:",num
    N=list(np.arange(10).astype(str))
    L = getL(num,RANGE)
    #print L
    c=0
    #print "N is ",N
    for x in L:
        #print "x is ",x
        #print " -- in i loop -- "
        for i in x:
            #print "i is ",i
            try:
                stri=str(i)
                k=N.index(stri)
            except ValueError:
                pass
            else:
                #print "k is ",k
                N.pop(k)
                #print "Popped ",str(i)," from N, and now N is ", N
            if len(N) == 0:
                #print "Breaking at Index ",c, " where L is ", L[c]
                return L[c]
        #print "c is ",c
        #print "--"
        c+=1
    return 'INSOMNIA'

fp = open("A-small-attempt0.in.txt")
tg = open("result.txt",'w')
for (i,line) in enumerate(fp):
    if i == 0:
        pass
    else:
        res = "Case #"+str(i)+": " + getInsom(int(line),RANGE)
        tg.write(res)
        tg.write("\n")
fp.close()
tg.close()