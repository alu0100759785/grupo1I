#!/usr/bin/python  
import random, sys
from math import *

A = 1
B = 3

def equal (expr1, expr2, A, B, n):
    i=0
    s=0
    while i<n:
	  a= random.uniform(A, B)
	  b= 2
	  if  eval (expr1)!= eval(expr2):
	    s+=1
	  i+=1
    porcentaje= s/float(n)*100
    return porcentaje

if __name__ == '__main__':
    
    expr1=sys.argv[1]
    expr2=sys.argv[2]
    A=float(sys.argv[3])
    B=float(sys.argv[4])
    n=int(sys.argv[5])
   
    print 'El porcentaje de fallos de la funcion es ', equal (expr1, expr2, A, B, n)
