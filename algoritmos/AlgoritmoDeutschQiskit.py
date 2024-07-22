from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram



# Definición de la función f(x) = x
def f(x):
    return 0

# Función que crea el oráculo basado en la función f(x)
def oracle(f):
    oracle_qc = QuantumCircuit(2, name='Oracle')
    # Aplicar la función f(x) = x
    if f(1) == 1 and f(0) == 0:
        oracle_qc.cx(0, 1)  # Aplicar una compuerta CNOT si f(1) es 1
    return oracle_qc

# Función que implementa el algoritmo de Deutsch-Josza
def deutsch_josza_algorithm(oracle):
    dj_circuit = QuantumCircuit(2, 1)
    dj_circuit.x(1)  # Preparar el qubit objetivo en el estado |1>
    dj_circuit.h([0, 1])  # Aplicar una compuerta Hadamard a ambos qubits
    dj_circuit.append(oracle, [0, 1])  # Aplicar el oráculo
    dj_circuit.h(0)  # Aplicar una compuerta Hadamard al qubit de entrada
    dj_circuit.measure(0, 0)  # Medir el qubit de entrada
    return dj_circuit

# Construir el circuito Deutsch-Josza
oracle_circuit = oracle(f)
dj_circuit = deutsch_josza_algorithm(oracle_circuit)

# Transpilar el circuito para el simulador cuántico
simulator = AerSimulator()

# Ejecutar el circuito en un simulador cuántico
compiled_circuit = transpile(dj_circuit, simulator)
result = simulator.run(compiled_circuit, shots=1024).result()

# Obtener los resultados
counts = result.get_counts()
print("Counts:", counts)

# Visualizar los resultados en un histograma
plot_histogram(counts)
