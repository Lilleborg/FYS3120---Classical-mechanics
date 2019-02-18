import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Plotting style
plt.style.use('bmh')
font = {'size'   : 16}
plt.matplotlib.rc('text', usetex=True)
plt.matplotlib.rc('font', **font)

r_0 = 1.
omega = 1.

t = np.linspace(0,pi,1000)

plt.figure()
plt.title('Orbit rotating rod, ' + r'\quad $r_0 = 1, \quad \omega = 1$')
plt.plot([1,1],[0,0],'ro',label='Initial position')
plt.plot(np.cosh(t)*np.cos(t),np.cosh(t)*np.sin(t))
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.axis('equal')
plt.tight_layout()
plt.savefig('./figurer/orbit_rod.png')
plt.show()