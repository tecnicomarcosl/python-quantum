import numpy as np

# Definimos dos matrices de 2x2
matriz_A = np.array([[1, 0],
                     [0, 0]])

matriz_B = np.array([[1, 0],
                     [0, 0]])

# Multiplicamos las dos matrices
resultado = np.matmul(matriz_A, matriz_B)

# Mostramos la transpuesta de la matriz A
print("\nLa transpuesta de la matriz A es:")
print(matriz_A.T)

# Mostramos el resultado
print("El resultado de la multiplicación de las matrices A y B es:")
print(resultado)
