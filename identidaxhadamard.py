import numpy as np

# Definir la matriz de identidad 2x2
I = np.array([[1, 0],
              [0, 1]])

# Definir la matriz de Hadamard
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

# Calcular el producto tensorial
producto_tensorial = np.kron(I, H)

print("Producto Tensorial:")
print(producto_tensorial)
