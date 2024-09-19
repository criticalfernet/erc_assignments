import numpy as np

#Question 1:
matrix1 = np.ndarray((10,1),int)
matrix1.fill(1)
matrix1[0::2] = 0
print(matrix1)

#Question 2:
matrix2 = np.random.rand(10)
print(matrix2)

#Question 3:
values = np.arange(1,16+1)
matrix3 = values.reshape((4,4))
subarr_index = 2
submat = matrix3[subarr_index:,subarr_index:]
print(matrix3)
print(submat)


#Question 4:
values = np.arange(1,10)
np.random.shuffle(values)
_matrix4 = values.reshape((1,9))
matrix4 = _matrix4.reshape((3,3))
print(matrix4)

#Question 5:
matrix5 = np.random.rand(3,4)

product = np.matmul(matrix4,matrix5)

print(product)


#Question 6:
sumval = matrix4.sum()
meanval = matrix4.mean()
minval = matrix4.min()
maxval = matrix4.max()
print(sumval)
print(meanval)
print(minval)
print(maxval)



