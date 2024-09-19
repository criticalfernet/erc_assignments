import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-13,13)
y = 3*x + 1

fig, ax = plt.subplots()
ax.plot(x,y)

plt.xlabel('x')
plt.xlim(-13,12)

plt.ylabel('y')
plt.ylim(min(y),max(y))

plt.show()

