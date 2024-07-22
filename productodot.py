import numpy as np

# Definir los vectores i y j
i = np.array([[1], [0], [0]])
j = np.array([[0], [1], [0]])

# Calcular el producto interno
producto_interno = np.dot(i.T, j)

print(producto_interno)
