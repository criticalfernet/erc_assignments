import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-10,11)
y = 3 * (x ** 2)

fig, ax = plt.subplots()
ax.plot(x,y,color='#ff0000',linestyle='dashed')


plt.show()
