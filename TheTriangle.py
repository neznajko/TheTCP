#!/usr/bin/env python3.6
################_###################################
#
# Problem 1: The Triangle
#      7
#     3 8
#    8 1 0
#   2 7 4 4
#  4 5 2 6 5 (Figure 1)
#
# Figure 1 shows  a number triangle. Write a program
# that calculates the highest  sum of numbers passed
# on  a  route that  starts  at  the  top  and  ends
# somewhere on the base.
# > Each step  can go  either diagonally down to the
#   left or diagonally down to the right.
# > The  number of  rows in  the triangle is  >1 but
#   <=100.
# > The numbers in the triangle,  all integers,  are
#   between 0 and 99.
#
# Input Data
# Data about  the number of rows in the triangle are
# first read from the INPUT.TXT file. In our example,
# INPUT.TXT appears as follows:
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
# Output  Data  The  highest sum  is written  as  an
# integer in the OUTPUT.TXT file. In our example:
# 30
################_###################################
# Becoz  of  its  fixed shape  we can  represent the
# binary  tree  as  an  array  similar to  the  heap
# data structure.
heap = [] # the heap
hsiz = 0  # heap size
mxsm = 0  # maximum sum
def fillHeap(file_name):
    """ Fill the heap from file_name. """
    global hsiz
    with open(file_name) as f:
        buf = f.readlines()
        buf = [line.split() for line in buf]
    for line in buf[1:]: # discard first line
        heap.extend([int(n) for n in line])
    ################################################
    hsiz = len(heap)
####################################################
def left(root): return ((2*root) + 1) # 0-based heap
####################################################
def isTerm(root):
    """ Ck if terminal node. """
    global hsiz
    return (not (root < hsiz))
    ################################################
####################################################
def ordeer(root, sm):
    """ Inorder search for maximum sum. """
    global hsiz, mxsm
    sm += heap[root] # previsit
    l = left(root) # get left child
    if isTerm(l): # Terminal Node?
        mxsm = max(mxsm, sm)
    else:
        ordeer(l, sm)
        ordeer(l + 1, sm)
    ################################################
    sm -= heap[root] # pstvisit
####################################################    
if __name__ == "__main__":
    fillHeap("INPUT.TXT")
    if 0: import pdb; pdb.set_trace()
    ordeer(0, 0)
    print(mxsm)
####################################################
# log: cat INPUT.TXT | ./TheTriangle.py
