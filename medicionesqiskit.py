from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt

#creamos un sistema de 3 qbits
W = Statevector([0, 1, 1, 0, 1, 0, 0, 0] / sqrt(3))
display(W.draw("latex"))

result, new_sv = W.measure([0])  # measure qubit 0
print(f"Measured: {result}\nState after measurement:")
display(new_sv.draw("latex"))


