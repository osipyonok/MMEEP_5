# tasks https://i.gyazo.com/9944a604f4298bef0adc63a83694ae69.png
# theory https://i.gyazo.com/5242e6127d20b1831949f3a80bdb6a73.png

from scipy.integrate import odeint
import matplotlib.pyplot as plt
from numpy import *
from scipy.optimize import broyden1


x0 = array([35, 3.857])
gamma = [0.37, 0.07]
alpha = [-5.68, 1.78]
beta = 0.55
eps = [1.38, 0.84]


def f(n, t=0):
    return [
        n[0] * (eps[0] - gamma[0] * n[0]) - (alpha[0] * n[0] * n[1]) / (1 + beta * n[0]),
        -n[1] * (eps[1] + gamma[1] * n[1]) + (alpha[1] * n[0] * n[1]) / (1 + beta * n[0])
    ]


t = linspace(0, 5,  10000)


N, infodict = odeint(f, x0, t, full_output=True)
# print(infodict['message'])

N_rabbits, N_foxes = [], []
for x, y in N:
    N_rabbits.append(x)
    N_foxes.append(y)

plt.figure('Task 4')
plt.subplot(1, 2, 1)
curves = plt.plot(t, N_rabbits, t, N_foxes)
plt.grid()


x_n1 = broyden1(f, [10, 10])  # or you can just wolfram your equation

values = linspace(0.5, 2, 150)
vcolors = plt.cm.autumn_r(linspace(0.7, 1, len(values)))

plt.subplot(1, 2, 2)
# trajectories
for v, col in zip(values, vcolors):
    P0 = [E * v for E in x_n1]
    P = odeint(f, P0, t)
    plt.plot( P[:, 0], P[:, 1], lw=0.1*v, color=col, label='P0=(%.f, %.f)' % ( P0[0], P0[1]))


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
plt.plot([0], [0], marker='o', markersize=3, color="black")
plt.plot([eps[0] / gamma[0]], [0], marker='o', markersize=3, color="black")

plt.xlim([x_n1[0] - 5, x_n1[0] + 5])
plt.ylim([x_n1[1] - 5, x_n1[1] + 5])

print('Точки спокою (при дійсних невід\'ємних х та у)')
print(array([0, 0]))
print(array([eps[0] / gamma[0], 0]))
print(x_n1)

plt.show()
