from numpy import *
from matplotlib.pyplot import *

print('Liczba punktow: ')
c = int(input())

t = linspace(1, 20, c)
y=sin(t)

plot(y)
show()