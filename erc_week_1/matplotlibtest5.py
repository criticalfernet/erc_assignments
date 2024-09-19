import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50) * 20
y = np.random.rand(50) * 20

fig, ax = plt.subplots()

ax.scatter(x,y,color="#0091d7",label="random points")

plt.xlabel("X values")
plt.ylabel("Y values")

plt.show()
