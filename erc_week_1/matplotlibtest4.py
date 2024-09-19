import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.01,10,100)

y1 = x**4
y2 = np.log(x)
y3 = np.exp(x)


fig, ax = plt.subplots()


plt.xlabel('x values')
plt.ylabel('y values')

ax.plot(x,y1,color='#ff0000',linestyle='solid')
ax.plot(x,y2,color='#00ff00',linestyle='dashed')
ax.plot(x,y3,color='#0000ff',linestyle='dotted')

plt.show()

