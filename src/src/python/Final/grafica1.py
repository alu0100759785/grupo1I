from matplotlib.pylab import *
# Mostrar mas de una representacion en el mismo lienzo 

diagrama1 = figure(1)


def g(x):
  
  return 1/(4*x)
  
def f(x):
#En este caso c vale 2
  
  return (0.125-(0.0625)*(x-2))

x = linspace(1, 3, 51)  # 51 puntos entre 1 y 3
y = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  y[i] = g(x[i])



x = linspace(1, 3, 51)  # 51 puntos entre 1 y 3

h = zeros(len(x))       # reserva memoria para y con elementos flotantes
for i in xrange(len(x)):
  h[i] = f(x[i])
  
plot0= plot(x,y, 'r')
plot1= plot(x,h,'b')
xlabel('x')
ylabel('y')

legend(['Funcion', 'Grado1'])
savefig('segunda.eps')
show()