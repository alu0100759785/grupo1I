#!/usr/bin/python
import  sys
from sympy import *
from math import *

symb_x = Symbol('x')



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

    sum+=((eval(str(derivada)))/(fac(i)))*((x-c)**i)
    print sum
  return sum
  
def fun(c):
  x=c
  func = 1/(4*symb_x)
  sum2= eval(str(func))
  return sum2
def error(c, symb_x, n):
  error=(fun(c))-(taylor(c, symb_x, n))
  return error
    
if __name__ == '__main__':
  n=int(sys.argv[1])
  c=float(sys.argv[2])
  x=float(sys.argv[3])
    
  print "El resultado de evaluar el ploinomio de Taylor de grado {0} en el punto {1} es {2}".format(n, symb_x, taylor(c, symb_x, n))
  print "El resultado de evaluar la funcion en el punto {0} es: {1}".format(c,fun(c))
  print "El error cometido por el polinomio de Taylor es de: {0}".format(error(c, symb_x, n))