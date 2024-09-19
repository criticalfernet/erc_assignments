import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,1.5*np.pi,50)

y = np.cos(x)

fig, ax = plt.subplots()

ax.plot(x,y)

plt.show()
