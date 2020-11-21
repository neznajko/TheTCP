########################################
NofDigits = 5
Dgts = ([0]*NofDigits)
FstDgt = 1 # First Digit
DgtSum = 8 # Digits Sum, both are program's input
MxLevl = (NofDigits - 1)
Start = ([0]*NofDigits)      # Domain Ranges
Stop = 10                    #
Step = ([1]*NofDigits)       #
Start[0] = Start[MxLevl] = 1 #
Step[MxLevl] = 2             # Odd Digits
Primez = []                  # list of all candidate primes lists
def toNumber():
    ''' Dgts list to number '''
    number = 0
    power = 1
    for d in reversed(Dgts):
        number += (d*power)
        power *= 10
    return number
# Again, from the book of Dasgupta et al.:
def modexp(x, y, n):
    """  y
       (x)mod(n)
    """
    if (y == 0): return 1
    z = modexp(x, (y >> 1), n) # floor(y / 2)
    if (y & 1): # odd
        return ((x*z*z)%n)
    else:
        return ((z*z)%n)
from random import randint
def primality2(n, k):
    ''' Ck if n is prime with error probability
        less than (1/2)**k
    '''
    m = n - 1
    for j in range(k):
        a = randint(1, m)        # [1, n - 1]
        if modexp(a, m, n) != 1: # Little Fermat Theorem
            return False         # n is not prime
    return True                  # passed
def Blk(levl):
    ''' Block of Backtrack Instructions '''
    for j in range(Start[levl], Stop, Step[levl]):
        if (DgtSum < (sum(Dgts[:levl]) + j)): break
        Dgts[levl] = j
        if (levl == MxLevl):
            if (DgtSum == sum(Dgts)) and primality2(toNumber(), 11):
                Primez.append(Dgts[:])
        else:
            Blk(1 + levl)
def BackTrack():
    '''**^**'''
    Blk(0) #\:)
