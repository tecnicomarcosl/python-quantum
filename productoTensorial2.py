import numpy as np

# Define las matrices
matrix1 = np.array([[1, 0, 0, 0], 
                    [0, 0, 0, 1], 
                    [0, 0, 1, 0], 
                    [0, 1, 0, 0]])

matrix2 = np.array([[1/np.sqrt(2), 1/np.sqrt(2), 0, 0], 
                    [1/np.sqrt(2), -1/np.sqrt(2), 0, 0], 
                    [0, 0, 1/np.sqrt(2), 1/np.sqrt(2)], 
                    [0, 0, 1/np.sqrt(2), -1/np.sqrt(2)]])

# Calcula el producto de Kronecker
#kronecker_product = np.kron(matrix1, matrix2)
kronecker_product=matrix1*matrix2
print(kronecker_product)
