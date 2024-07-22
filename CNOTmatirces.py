import numpy as np
from qiskit.quantum_info import Statevector

C = np.array([0, 1])  # |1⟩
T = np.array([1, 0])  # |1⟩

# Definir la matriz de la compuerta CNOT
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# Combinar los estados de los qubits en un solo estado de dos qubits
estado = np.kron(C, T)

# Aplicar la compuerta CNOT al estado
estado_final = np.dot(CNOT, estado)

print("Estado final después de aplicar la compuerta CNOT:", estado_final)

# Convertir el estado final a un objeto Statevector de Qiskit
estado_final_qiskit = Statevector(estado_final)

# Convertir los estados iniciales en vectores de estado cuántico utilizando Statevector
estado_C = Statevector(C.flatten())
estado_T = Statevector(T.flatten())
estado_tensorial = Statevector(estado.flatten())

# Mostrar los resultados en formato LaTeX
print("Matriz C:")
print(C)
display(estado_C.draw("latex"))

print("\nMatriz T:")
print(T)
display(estado_T.draw("latex"))

print("Estado luego del producto tensorial de los 2 qbits:")
print(estado)
display(estado_tensorial.draw("latex"))

# Mostrar los resultados en formato LaTeX
print("Estado final después de aplicar la compuerta CNOT:")

display(estado_final_qiskit.draw("latex"))
