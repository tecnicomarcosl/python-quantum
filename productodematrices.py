import numpy as np
from qiskit.quantum_info import Statevector

O = np.array([[1,0],
              [0,1]])

L = np.array([[0,1],
              [1,0]])

# Convertir las matrices en vectores de estado cuántico utilizando Statevector
estado_O = Statevector(O.flatten())
estado_L = Statevector(L.flatten())

# Calcular el producto interno entre los vectores de estado
producto_interno = np.inner(estado_L.data, estado_O.data)
estado_producto = Statevector(producto_interno.flatten())

# Mostrar los resultados en formato LaTeX
print("Matriz O:")
display(estado_O.draw("latex"))

print("\nMatriz L:")
display(estado_L.draw("latex"))

print("\nEstado del vector O:")
display(estado_O.draw("latex"))

print("\nEstado del vector L:")
display(estado_L.draw("latex"))

print("\nProducto interno:")
print(estado_producto.draw())
