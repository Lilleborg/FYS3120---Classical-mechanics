import numpy as np
import matplotlib.pyplot as plt

# Plotting style
plt.style.use('bmh')
font = {'size'   : 16}
plt.matplotlib.rc('text', usetex=True)
plt.matplotlib.rc('font', **font)

k = 5

## Not in use, trying to find theta from a given point B
# B = [1,-0.5]
# b = 2*B[1]/k**2
# a = 2*B[0]/k**2
# x = A - sqrt(-B (B + 2))
#theta_B = a +- np.sqrt(-b * (b+2))


theta = np.linspace(0,3*np.pi/2,1000)
theta_B = np.pi

x = 0.5 * k**2 *(theta - np.sin(theta))
y = 0.5 * k**2 *(np.cos(theta)-1)
x_straight = np.linspace(0,x[-1],100)
y_straight = -2/np.pi*x_straight

x_B = 0.5*k**2 *(theta_B-np.sin(theta_B))
y_B = 0.5*k**2 *(np.cos(theta_B)-1)

index_B = np.argmin(np.abs(y-y_B))
B = [x[index_B],y[index_B]]

plt.plot(x,y,marker='o',label= r'$y(\theta)$',markevery=[0,-1])
plt.plot(*B,'ro',label='Point B')
plt.plot(x_straight,y_straight,label='Straight line')
plt.axis('equal')
plt.title(r'The Brachistochrone curve, $\theta \in [0,\frac{3\pi}{2}]$, $k=5$')
plt.ylabel('y')
plt.xlabel('x')
plt.legend()
plt.tight_layout()
plt.savefig('brachistochrone.pdf')
plt.show()
