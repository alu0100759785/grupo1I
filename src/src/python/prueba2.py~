#!/usr/bin/python
import  sys
from sympy import *
from math import *

symb_x = Symbol('x')

n=3
c=2.0
def fac(i):
    if i == 0:
	return 1
    else:
	return i * fac(i-1)
	
def taylor(c, symb_x, n):
  func = 1/(4*symb_x)
  sum=0
  for i in range(n+1):
    derivada= diff(func,symb_x, i)
    print derivada
    x=4.0
    sum+=((eval(str(derivada)))/(fac(i)))*((x-c)**i)
    print sum
  return sum
    
if __name__ == '__main__':
  
  print "El resultado de evaluar el ploinomio de taylor de grado {0} en el punto {1} es {2}".format(n, symb_x, taylor(c, symb_x, n))