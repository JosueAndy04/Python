import numpy as np
import pandas as pd

array_unidim = np.array([1, 2, 3, 4, 5])

array_bidim = np.array([[1, 2, 3], [4, 5, 6]])

array_tridim = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

(
    array_unidim.shape,
    array_bidim.ndim,
    array_tridim.dtype,
    array_unidim.size,
    type(array_bidim),
)

datos = pd.DataFrame(array_bidim)
print(datos)

unos = np.ones((4, 3))
ceros = np.zeros((2, 4, 3))
print(unos)
print(ceros)

array_1 = np.arange(0, 101, 5)
array_2 = np.random.randint(0, 10, (2, 5))
array_3 = np.random.random((3, 5))

np.random.seed(27)

array_4 = np.random.randint(0, 10, (3, 5))

print(array_1)
print(array_2)
print(array_3)
print(array_4)

np.unique(array_4)
array_4[1]
array_4[:2]

array_4[:2, :2]

array_5 = np.random.randint(0, 10, (3, 4))
array_6 = np.ones((3, 4))

array_5 + array_6

array_7 = np.ones((4, 3))

# print(array_6 + array_7) Error

array_8 = np.ones((4, 3))
array_8 - array_7

array_9 = np.random.randint(1, 5, (3, 3))
array_10 = np.random.randint(1, 5, (3, 3))

array_9 * array_10

array_9**2

np.sqrt(array_9)

array_9.mean()

array_9.max()

array_9.min()

array_11 = array_9.reshape((9, 1))

array_11.T

array_12 = array_9 > array_10

array_12.dtype

array_12 == array_12
array_9 > 2

np.sort(array_9)
