import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-13,13)
y = 3*x + 1
fig1, ax1 = plt.subplots()
ax1.plot(x,y)
plt.xlabel('x')
plt.xlim(-13,12)
plt.ylabel('y')
plt.ylim(min(y),max(y))
ax1.plot(x,y,color='#ffdf50')

x = np.arange(-10,11)
y = 3 * (x ** 2)
fig2, ax2 = plt.subplots()
plt.xlim(-10,10)
plt.ylim(min(y),max(y))
ax2.plot(x,y,color='#e94251',linestyle='dashed')


x = np.linspace(0,1.5*np.pi,50)
y = np.cos(x)
fig3, ax3 = plt.subplots()
plt.xlim(0,2*np.pi)
plt.ylim(min(y),max(y))
ax3.plot(x,y,color='#b77aff')


x = np.linspace(0.01,10,100)
y1 = x**4
y2 = np.log(x)
y3 = np.exp(x)
fig4, ax4 = plt.subplots()
plt.xlabel('x values')
plt.ylabel('y values')
plt.xlim(0,10)
plt.ylim(-1000,max(max(y1),max(y2),max(y3)))
ax4.plot(x,y1,color='#ff0000',linestyle='solid')
ax4.plot(x,y2,color='#00ff00',linestyle='dashed')
ax4.plot(x,y3,color='#0000ff',linestyle='dotted')


x = np.random.rand(50) * 20
y = np.random.rand(50) * 20
fig5, ax5 = plt.subplots()
plt.xlim(0,20)
plt.ylim(min(y),max(y))
ax5.scatter(x,y,color="#00a1c7",label="random points")
plt.xlabel("X values")
plt.ylabel("Y values")


ax1.set_facecolor('#eafff5')
ax2.set_facecolor('#eafff5')
ax3.set_facecolor('#eafff5')
ax4.set_facecolor('#eafff5')
ax5.set_facecolor('#eafff5')


plt.show()
