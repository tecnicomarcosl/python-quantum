import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex

# Definir los estados |0> y |1>
O = np.array([[1],
              [0]])

L = np.array([[0],
              [1]])

# Definir la matriz de Hadamard
H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]])

# Calcular el resultado de aplicar la compuerta Hadamard a los estados |0> y |1>
resultado_0 = np.dot(H, O)
resultado_1 = np.dot(H, L)

# Convertir los resultados en objetos Statevector de Qiskit
estado_0 = Statevector(resultado_0.flatten())
estado_1 = Statevector(resultado_1.flatten())

# Mostrar la matriz de Hadamard
print("Matriz de Hadamard:")
print(H)

# Mostrar la matriz de Hadamard . |0>
print("Matriz de Hadamard. |0>")
print(resultado_0)

# Mostrar la matriz de Hadamard . |1>
print("Matriz de Hadamard . |1>:")
print(resultado_1)

# Mostrar los resultados en notación de Dirac de Qiskit
print("Resultado de aplicar Hadamard a |0> en notación de Dirac de Qiskit:")
display(estado_0.draw("latex"))

print("Resultado de aplicar Hadamard a |1> en notación de Dirac de Qiskit:")
display(estado_1.draw("latex"))

