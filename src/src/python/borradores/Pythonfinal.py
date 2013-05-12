#!/usr/bin/python
import  sys
from sympy import *
from math import *

symb_c = Symbol('c')
symb_x = Symbol('x')
func = 1/(4*symb_c)



def fac(i):
    if i == 0:
	return 1
    else:
	return i * fac(i-1)
	
def taylor(c, x, n):
  
  sum=0
  for i in range(n):
    derivada= diff(func, symb_c, i)

    sum+=((eval(str(derivada)))/((fac(i)))*((x-c)**(i)))
    
  return sum
  
def fun(x):
  
  func = 1/(4*symb_x)
  sum2= eval(str(func))
  return sum2
  
  
def error(c, x, n):
  error=(abs((taylor(c, x, n))-(fun(x))))/(fun(x)) * 100
  return error
    
if __name__ == '__main__':
  n=int(sys.argv[1])
  x=float(sys.argv[2])
  c=float(sys.argv[3])
    
  print "El resultado de evaluar el ploinomio de Taylor de grado {0} en el punto {1} es {2}".format(n, x, taylor(c, x, n))
  print "El resultado de evaluar la funcion en el punto {0} es: {1}".format(c,fun(x))
  print "El error cometido por el polinomio de Taylor es de: {0}".format(error(c, x, n))