import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Plotting style
plt.style.use('bmh')
font = {'size'   : 16}
plt.matplotlib.rc('text', usetex=True)
plt.matplotlib.rc('font', **font)
#plt.rcParams["figure.figsize"] = [14,8]
#plt.matplotlib.rc('figure.figsize',(14,8))

def RHS(y,t,p,m):
    g = 9.81
    r,v,phi,omega = y
    return [v,
            p**2/m**2/r**3/2-g/2,
            omega,
            -2*v*omega/r]

# Initial conditions and constants
m = 1
p = 1
l = 1
v0 = 0.5
phi0 = 0
omega0 = p/m/l**2

init = [l,v0,phi0,omega0]
t = np.linspace(0,20,1000)

solution = odeint(RHS,init,t,args=(p,m))
r,v,phi,omega = solution[:,0],solution[:,1],solution[:,2],solution[:,3]

while (phi>2*np.pi).any():
    phi[phi>2*np.pi] -= 2*np.pi

plt.figure()
plt.title('Coordinates vs time')
plt.plot(t,r,label=r'$r(t)$')
plt.plot(t,phi,label=r'$\phi(t)$')
plt.plot(t,omega,label=r'$\omega(t)$')
plt.plot(t,v,label=r'$v(t)$')
plt.xlabel('Time')
plt.legend()
plt.grid()
plt.savefig('./figurer/components_vs_time.pdf')

plt.figure()
plt.title('Motion of mass 2 in the plane')
plt.plot(r*np.cos(phi),r*np.sin(phi))
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.savefig('./figurer/polar_movement.pdf')



plt.show()