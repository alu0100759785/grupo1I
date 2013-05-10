from matplotlib.pylab import *
# Mostrar mas de una representacion en el mismo lienzo 

diagrama1 = figure(1)

# la figura tendra 2 filas y 1 columna y se quiere trazar en la primera
subplot(211)

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
  

x = linspace(1, 3, 51)  # 51 puntos entre 0 y 3
y = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  y[i] = g(x[i])



x = linspace(1, 3, 51)  # 51 puntos entre 0 y 3

h = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  h[i] = f(x[i])
  
x = linspace(1, 3, 51)  # 51 puntos entre 0 y 3
z = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  z[i] = t(x[i])
  
x = linspace(1, 3, 51)  # 51 puntos entre 0 y 3
w = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  w[i] = p(x[i])

plot0= plot(x,y, 'r')
plot1= plot(x,h,'b')
plot2= plot(x,z,'y')
plot2= plot(x,w,'g')

xlabel('x')
ylabel('y')

legend(['Funcion', 'Grado1', 'Grado2', 'Grado3'])


# para trazar en la segunda 
#subplot(212)

#l= ['1e-1', '1e-2','1e-3', '1e-4', '1e-5']
#x=[1, 2, 3, 4, 5]
#xlim(0.0, 6.0)
#p=[17.1, 64.9, 65.2, 67.1, 65.2]
#xticks(x,l)
#ylim(0.0, 100.0)
#plot(x, p, 'go')


# mostrar por la consola el resultado
show()
