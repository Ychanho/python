import numpy as np

list_mat = [[1,2,3],
            [3,6,9],
            [2,4,6]]
matrix = np.array(list_mat)
print(matrix)
print(matrix.shape)

random_matrix = np.random.rand(3,3)
print(random_matrix)
zero_matrix = np.zeros((3,3))
print(zero_matrix)

# ma = np.random.ra
# random.rand 와 random의 차이?

#matrix slicing
print('matrox slicing')
print(matrix[1,2])

print(matrix[1])

print(matrix[1:3])

print(matrix[:, 1])

print(matrix[1:, 1:])

#array operation
print('arry operation')
matrix2 =np.array([[1,2,3,],
                  [4,5,6,],
                  [7,8,9]])

vector = np.array([[1],
                  [2],
                  [3]])
print(vector.shape)
print(matrix2 * vector)
print(matrix2.dot(vector))