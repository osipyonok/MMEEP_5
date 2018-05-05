# tasks https://i.gyazo.com/9944a604f4298bef0adc63a83694ae69.png
# theory https://i.gyazo.com/5242e6127d20b1831949f3a80bdb6a73.png

from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import *

''' math model of ukraine, lol
x0 = array([13.5, 7])
gamma = [2.5, 1]
eps = [4, 2]
'''


x0 = array([200, 100])
gamma = [0.001, 0.01]
eps = [0.02, 2]



def f(n, t=0):
    return [
        eps[0] * n[0] - gamma[0] * n[0] * n[1],
        -eps[1] * n[1] + gamma[1] * n[0] * n[1]
    ]


t = linspace(0, 150,  10000)


N, infodict = odeint(f, x0, t, full_output=True)
print(infodict['message'])

N_rabbits, N_foxes = [], []
for x, y in N:
    N_rabbits.append(x)
    N_foxes.append(y)

plt.figure('Task 1')
plt.subplot(1, 2, 1)
curves = plt.plot(t, N_rabbits, t, N_foxes)
plt.grid()

x_n1 = array([eps[1] / gamma[1], eps[0] / gamma[0]])


values = linspace(0.1, 1.2, 50)
vcolors = plt.cm.autumn_r(linspace(0.1, 1, len(values)))

plt.subplot(1, 2, 2)
# trajectories
for v, col in zip(values, vcolors):
    P0 = [E * v for E in x_n1]
    P = odeint(f, P0, t)
    plt.plot( P[:, 0], P[:, 1], lw=0.5*v, color=col, label='P0=(%.f, %.f)' % ( P0[0], P0[1]))


ymax = plt.ylim(ymin=0)[1]
xmax = plt.xlim(xmin=0)[1]
# Define number of points
nb_points = 20
# Define x and y ranges
x = linspace(x_n1[0] - 5, x_n1[0] + 5, nb_points)
y = linspace(x_n1[1] - 5, x_n1[1] + 5, nb_points)
# Create meshgrid
X1 , Y1 = meshgrid(x,y)
# Calculate growth rate at each grid point
DX1, DY1 = f([X1, Y1], 0)
# Direction at each grid point is the hypotenuse of the prey direction and the
# predator direction.
M = (hypot(DX1, DY1))
# This is to avoid any divisions when normalizing
M[M == 0] = 1.
# Normalize the length of each arrow (optional)
DX1 /= M
DY1 /= M

Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.plasma)
plt.plot([x_n1[0]], [x_n1[1]], marker='o', markersize=3, color="blue")

plt.xlim([x_n1[0] - 5, x_n1[0] + 5])
plt.ylim([x_n1[1] - 5, x_n1[1] + 5])

print('Точки спокою (при дійсних невід\'ємних х та у)')
print(array([0, 0]))
print(x_n1)

plt.show()
