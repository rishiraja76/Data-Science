#importing package 
import numpy as np
import matplotlib.pyplot as plt

#declaring arrays
x = np.arange(0,100)
y = x*2
z = x**2

#plotting x vs y
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()

#plotting x vs y inside another plot of x vs y
fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.2,0.2])
ax1.plot(x,y)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax2.plot(x,y)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
plt.show()

#plotting x vs y with a limiter inside another plot of x vs z
fig=plt.figure()
ax1=fig.add_axes([0,0,1,1])
ax2=fig.add_axes([0.2,0.5,0.4,0.4])
ax1.plot(x,z)
ax1.set_xlabel('X')
ax1.set_ylabel('Z')
ax2.set_xlim(20,22)
ax2.set_ylim(30,50)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('zoom')
ax2.plot(x,y)
plt.show()

#creating a subplot with two plots of x vs y and x vs z
fig,ax= plt.subplots(nrows=1, ncols=2)
ax[0].plot(x,y,color="blue",linestyle="--",linewidth=2)
ax[1].plot(x,z,color="red",linestyle="-",linewidth=2)
plt.show()

#creating a vertical subplot with two plots of x vs y and x vs z
fig,ax= plt.subplots(nrows=1, ncols=2,figsize=(16,2))
ax[0].plot(x,y,color="blue",linestyle="-",linewidth=2)
ax[0].set_xlabel('x')
ax[0].set_ylabel('y')
ax[1].plot(x,z,color="red",linestyle="--",linewidth=2)
ax[1].set_xlabel('x')
ax[1].set_ylabel('z')
plt.show()