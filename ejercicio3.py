import numpy as np

# Definir el estado de dos qubits como un vector columna
psi = np.array([[0], [0], [0], [0]])

# Definir la matriz de la compuerta CNOT
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# Aplicar la compuerta CNOT al estado de dos qubits
nuevo_estado = np.dot(CNOT, psi)

print("Nuevo estado después de aplicar la compuerta CNOT:")
print(nuevo_estado)
