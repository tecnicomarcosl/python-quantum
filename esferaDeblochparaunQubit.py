from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
from qiskit.quantum_info import Statevector

# Creamos un circuito cuántico con 1 qubit
qc = QuantumCircuit(1)

# Seleccionamos el simulador Aer
backend = Aer.get_backend('statevector_simulator')

# Ejecutamos el circuito en el simulador
result = backend.run(qc).result()

# Obtenemos el estado vectorial resultante
statevector = result.get_statevector()

# Imprimimos el estado vectorial
print("Estado vectorial:", statevector)

# Visualizamos el estado en la esfera de Bloch
display(plot_bloch_multivector(statevector))
