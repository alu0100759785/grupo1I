#!/usr/bin/python  
import  sys
from math import *
from interpolacion import equal

L=[
('1/(4*a)','(1/(4*b))-((1/(4*b**2)*(a-b)))'),
('1/(4*a)','(1/(4*b))-((1/(4*b**2)*(a-b))+((1/(4*b**3))*(a-b)**2))'),
('1/(4*a)','(1/(4*b))-((1/(4*b**2)*(a-b))+((1/(4*b**3))*(a-b)**2)-((1/(4*b**4))*(a-b)**3))'),
('1/(4*a)','(1/(4*b**2)*(a-b))+((1/(4*b**3))*(a-b)**2)-((1/(4*b**4))*(a-b)**3)+((3/(2*b**5))*(a-b)**4)')

]

if __name__ == '__main__':
    A=float(sys.argv[1])
    B=float(sys.argv[2])
    n=int(sys.argv[3])
    
    for t in L:
      print "%25s %25s %10.1f"% (t[0], t[1], equal(t[0],t[1], A,B,n))
      
      
      