from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram

# Función constante
def constant_oracle(qc):
    pass  # No se aplican puertas, el qubit de salida permanece en |0⟩

# Función balanceada
def balanced_oracle(qc):
    qc.cx(0, 2)  # Puerta CNOT entre el primer qubit de entrada y el qubit de salida
    qc.cx(1, 2)  # Puerta CNOT entre el segundo qubit de entrada y el qubit de salida

# Creación del circuito cuántico
qc = QuantumCircuit(3, 2)

# Superposición en los dos qubits de entrada
qc.h([0,1])

# Puerta X y H en el qubit de salida
qc.x(2)
qc.h(2)

# Aplicación de la función constante o balanceada
# constant_oracle(qc)
balanced_oracle(qc)

# Inversión de la superposición en los qubits de entrada
qc.h([0,1])

# Medición de los qubits de entrada
qc.measure([0,1], [0,1])

# Simulación del circuito y visualización de resultados
simulator = Aer.get_backend('qasm_simulator')
compiled_circuit = transpile(qc, simulator)
qobj = assemble(compiled_circuit)
results = simulator.run(compiled_circuit).result()
counts = results.get_counts()
print(counts)
display(plot_histogram(counts))
