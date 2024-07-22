import numpy as np
from qiskit.quantum_info import Statevector
from qiskit.visualization import array_to_latex

# Definir las matrices H e I
H = np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
              [1/np.sqrt(2), -1/np.sqrt(2)]])

I = np.array([[1, 0],
              [0, 1]])

# Calcular el producto tensorial de I y H
producto_tensorial = np.kron(I, H)

# Calcular M * (I ⊗ H)
M = np.array([[1, 0, 0, 0],
              [0, 0, 0, 1],
              [0, 0, 1, 0],
              [0, 1, 0, 0]])
U = np.dot(M, producto_tensorial)

# Calcular U|00>
resultado_00 = np.dot(U, np.array([1, 0, 0, 0]))
resultado_00_estado = Statevector(resultado_00)

# Calcular U|01>
resultado_01 = np.dot(U, np.array([0, 1, 0, 0]))
resultado_01_estado = Statevector(resultado_01)

# Calcular U|10>
resultado_10 = np.dot(U, np.array([0, 0, 1, 0]))
resultado_10_estado = Statevector(resultado_10)

# Calcular U|11>
resultado_11 = np.dot(U, np.array([0, 0, 0, 1]))
resultado_11_estado = Statevector(resultado_11)

# Mostrar los resultados en notación de Dirac de Qiskit
print("Resultado de U|00> en notación de Dirac de Qiskit:")
display(resultado_00_estado.draw("latex"))

print("Resultado de U|01> en notación de Dirac de Qiskit:")
display(resultado_01_estado.draw("latex"))

print("Resultado de U|10> en notación de Dirac de Qiskit:")
display(resultado_10_estado.draw("latex"))

print("Resultado de U|11> en notación de Dirac de Qiskit:")
display(resultado_11_estado.draw("latex"))

