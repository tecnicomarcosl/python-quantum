import numpy as np

# Definimos la matriz H
H = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [1/np.sqrt(2), -1/np.sqrt(2)]])

# Definimos la matriz I
I = np.array([[1, 0],
              [0, 1]])

# Calculamos el producto tensorial de H e I usando NumPy
J = np.kron(I, H)

# Configuramos la precisión de impresión a 4 decimales
np.set_printoptions(precision=2)

# Imprimimos el producto tensorial en el formato deseado
print("El producto de H e I es:")
print(J)


from sympy import Matrix, tensorproduct, sqrt

# Definimos la matriz H
H = Matrix([[1/sqrt(2), 1/sqrt(2)],
            [1/sqrt(2), -1/sqrt(2)]])

# Definimos la matriz I
I = Matrix([[1, 0],
            [0, 1]])

# Calculamos el producto tensorial de H e I usando SymPy
J = tensorproduct(H, I)

# Imprimimos el resultado
print("El producto de H e I es:")
print(J)
