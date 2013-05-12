from matplotlib.pylab import *
# Mostrar mas de una representacion en el mismo lienzo 

diagrama1 = figure(1)

# la figura tendra 2 filas y 1 columna y se quiere trazar en la primera


def g(x):
  
  return 1/(4*x)
  
def f(x):
#En este caso c vale 2
  
  return (0.125-(0.0625)*(x-2))
  
def t(x):
#En este caso c vale 2
  
  return ((0.125-(0.0625)*(x-2))+(0.03125)*(x-2)**2)
  
def p(x):
#En este caso c vale 2
 
  return ((0.125-(0.0625)*(x-2))+(0.03125)*(x-2)**2-(0.015625)*(x-2)**3)
  

x = linspace(1, 30, 100)  # 51 puntos entre 0 y 3
y = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  y[i] = g(x[i])



x = linspace(1, 30, 100)  # 51 puntos entre 0 y 3

h = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  h[i] = f(x[i])
  
x = linspace(1, 30, 100)  # 51 puntos entre 0 y 3
z = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  z[i] = t(x[i])
  
x = linspace(1, 30, 100)  # 51 puntos entre 0 y 3
w = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  w[i] = p(x[i])

plot0= plot(x,y, 'r')
plot1= plot(x,h,'b')
plot2= plot(x,z,'y')
plot3= plot(x,w,'g')

xlabel('x')
ylabel('y')

legend(['Funcion', 'Grado1', 'Grado2', 'Grado3'])
show ()