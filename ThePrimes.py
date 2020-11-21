#!/usr/bin/env python3.6
# 
import BackTrack
import sys
BackTrack.FstDgt = int(sys.argv[1])
BackTrack.DgtSum = int(sys.argv[2])

BackTrack.BackTrack()

# paätifn
frontz = []
def doesn_thaaf():
    '''"""*****``**0**"""'''
    key = (fstDgt,)
    for p in Dict[key]:
        if (not (0 in p)):
            frontz.append(p)

class Testo:
    ''' _esting Tes_ing te_ting '''
    def primez():
        for i in range(10):
            pz = BackTrack.Primez[i]
            print("%d: %d" % (i, len(pz)))
            print(*pz, sep='\n')
    def boom(): sys.exit(1)

# Ready to Chess!?
fstDgt    = BackTrack.FstDgt
prmz      = BackTrack.Primez
n         = BackTrack.NofDigits
sqr       = [[0 for j in range(n)] for i in range(n)]
sqr[0][0] = fstDgt
def dumpSqr(): # 
    '''v^T<^he|D-um\/p'''
    print(*sqr, sep='\n', end='\n\n')
Dict = {} # The Dict
def insert(p):
    """ p is a list of prime number digits e.g:
        [1, 0, 7], create if not exist this keys:
        (1,), (1, 0) and push p to them.
    """
    for j in range(1, n):
        key = tuple(p[:j])
        if (not (key in Dict)):
            Dict[key] = [p]
        else:
            Dict[key].append(p)

for p in prmz: insert(p) # The Fill

# I'm readzhy tchou Gou, Vet'z Gou!!
def setDgnl(p):
    '''Diagonally'''
    for j in range(1, n):
        sqr[j][j] = p[j] # jj - ['zhizhi:] The Best Chinese Rapper (TBCR)
def setHorz(levl, p):
    """ Paguo Xopu3oHT """
    i = (levl - 1)
    for j in range(levl, n):
        sqr[i][j] = p[j]
def setVert(levl, p):
    """ Vera Verto """
    j = (levl - 1)
    for i in range(levl, n):
        sqr[i][j] = p[i]
def getVrtKey(lvel):
    """ Get to the point """
    j = lvel - 1 # sqr vertical index
    return tuple([sqr[i][j] for i in range(lvel)])
def getHrzKey(lvel):
    ''' Yeah! '''
    i = lvel - 1 # sqr horizontal index
    return tuple([sqr[i][j] for j in range(lvel)])
def TheFunction():
    '''--_--'''
    key = (fstDgt,)
    for d in Dict[key]:
        setDgnl(d)
        for h in frontz:
            setHorz(1, h)
            for v in frontz:
                setVert(1, v)
                Vrooo(2)
def TheCk():
    "ck if last row, last col, and 2nd diag are primies"
    # The Column:
    BackTrack.Dgts[:] = [sqr[i][(n - 1)] for i in range(n)]
    if (sum(BackTrack.Dgts) != BackTrack.DgtSum): return False
    nmba = BackTrack.toNumber()
    if not BackTrack.primality2(nmba, 13): return False # Very Folz
    # The Row:
    BackTrack.Dgts[:] = sqr[(n - 1)]
    if (sum(BackTrack.Dgts) != BackTrack.DgtSum): return False
    nmba = BackTrack.toNumber()
    if not BackTrack.primality2(nmba, 14): return False # Wery Wery
    # The Diagonal:
    BackTrack.Dgts[:] = [sqr[(n - 1 - j)][j] for j in range(n)]
    if (sum(BackTrack.Dgts) != BackTrack.DgtSum): return False
    nmba = BackTrack.toNumber()
    if not BackTrack.primality2(nmba, 15): return False # Xa-Xa
    return True
    
def Vrooo(lvel):
    ''''''""""""
    if lvel == n:
        if TheCk():
            dumpSqr()
        return
    vrtKey = getVrtKey(lvel)
    if not (vrtKey in Dict): return
    hrzKey = getHrzKey(lvel)
    if not (hrzKey in Dict): return
    for v in Dict[vrtKey]:
        setVert(lvel, v)
        for h in Dict[hrzKey]:
            setHorz(lvel, h)
            Vrooo(lvel + 1)
            
doesn_thaaf()
TheFunction()
Testo.boom()
# log:
# To run the program write:
# ./ThePrimes.py 1 11,
# to change the number of digits edit NofDigits in
# BackTrack.py
