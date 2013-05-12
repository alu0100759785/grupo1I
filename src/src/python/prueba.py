#!/usr/bin/python
import  sys
from sympy import *
from math import *

symb_x = Symbol('x')

n=4
def fac(i):
    if i == 0:
	return 1
    else:
	return i * fac(i-1)
	
def tylor(c, sim_x, n):
  func = 1/(4*symb_x)
  sum=0

  for i in range(n+1):
    derivada= diff(func,simb_x, i)
    x=3.0
    sum+=((eval(str(derivada))/(fac(i)))*(symb_x-c)

if __name__ == '__main__':
  
  print "El resultado de evaluar el polinomio de Tyalor de grado {0} en el punto {1} es {2}".format(n, x, taylor(c, sim_x, n))

    