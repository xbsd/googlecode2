import numpy as np
import numexpr as ne
import math
import datetime

def isPrime2(n):
    """Returns True if n is prime."""
    a=5
    v=2
    if n % 2 == 0 or n % 3 == 0:
        return False
    if n == 2 or n == 3:
        return True
    while a * a <= n:
        if n % a == 0:
            return False
        a=a+v
        v=6-v
    return True

def isPrime(n):
    return all(n%i for i in xrange(2, int(math.sqrt(n))+1))

def primeListCheck(valList):
    for i in valList:
        PrimeCheck = isPrime2(i)
        if PrimeCheck:
            print i
            return PrimeCheck
    return PrimeCheck

def getDivisor(NUM):
    for i in range(2,int(math.sqrt(NUM))+1):
        if NUM%i==0:
            return i

def baseN(candidate, base, DIG):
    candidateList = np.array([int(i) for i in candidate])
    powN = [base**x for x in (range(DIG))][::-1]
    return sum(candidateList*powN)

def isPrime(n):
    return all(n%i for i in xrange(2, n))

def isJamCoin(candidate):
    DIG = len(candidate)
    coinVal = [baseN(candidate,i,DIG) for i in range(2,11)]
    primeCheck = primeListCheck(coinVal)
    if primeCheck == False:
        return (True,candidate, coinVal)
    return (False,False)

def getCandidates(DIG):
    BINARY=np.array([2**i for i in range(DIG)])[::-1]

    MIN=sum(BINARY*np.array([int(imin) for imin in "1"+(DIG-1)*"0"]))
    MAX=sum(BINARY*np.array([int(imax) for imax in DIG*"1"]))
    #print BINARY
    #print MAX

    NUMLIST = np.arange(MIN, MAX+1)
    BINLIST = np.array(["{0:b}".format(i) for i in NUMLIST])
    BB = [[i[-1]=='1'] for i in BINLIST]
    BBI = np.array([i[0] for i in BB])

    CANDIDATES = BINLIST[BBI]
    return CANDIDATES

def getFinalCoins(DIG,NUMTOGET):
    FINAL=[]
    GC = getCandidates(DIG)
    GCX = np.random.choice(GC,GC.shape[0],replace=False)
    #GCX=GC
    for i in GCX:
        J = isJamCoin(i)
        if J[0]==True:
            FINAL.append(J)
            print str(datetime.datetime.now()),"  Found Value: ",str(len(FINAL)), " => ", str(J)
            if len(FINAL)==NUMTOGET:
                return FINAL

def final(DIG, NUMTOGET):
    Z = getFinalCoins(DIG, NUMTOGET)
    for (i,j,k) in Z:
        RESULT = [j,[getDivisor(v) for v in k]]
        print str(RESULT[0]) + " " + " ".join(str(item) for item in RESULT[1])

def finalSave(inputFile):
    fp = open(inputFile)
    saveFile = "result_"+inputFile
    tg = open(saveFile,'w')
    tg.write("Case #1:")
    tg.write("\n")
    
    for (ix, line) in enumerate(fp):
        if ix==0:
            pass
        else:
            val = line.split(" ")
            DIG=int(val[0])
            NUMTOGET=int(val[1])
    
    Z = getFinalCoins(DIG, NUMTOGET)
    for (i,j,k) in Z:
        RESULT = [j,[getDivisor(v) for v in k]]
        RESWRITE = str(RESULT[0]) + " " + " ".join(str(item) for item in RESULT[1])
        tg.write(RESWRITE)
        tg.write("\n")
    fp.close()
    tg.close()


