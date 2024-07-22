from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram

# Creamos un circuito cuántico con 2 qubits y 2 bits clásicos
qc = QuantumCircuit(8, 8)

# Aplicamos compuertas Hadamard a todos los qubits
qc.h(range(8))

# Medimos todos los qubits
qc.measure(range(8), range(8))

# Seleccionamos el simulador Aer
simulator = AerSimulator()

# Transpilamos el circuito para el simulador
qc_sim = transpile(qc, simulator)

# Ejecutamos el circuito transpilado en el simulador
result = simulator.run(qc_sim, shots=1000000).result()

# Obtenemos los conteos de cada resultado
counts = result.get_counts()

# Contamos cuántas veces se repite el mismo resultado
repeated_results = {result: count for result, count in counts.items() if count > 1}

# Mostramos los resultados y cuántas veces se repitieron
print("Resultados de la medición:", counts)
print("Resultados repetidos:", repeated_results)

# Mostramos el resultado con mayor frecuencia
most_frequent_result = max(counts, key=counts.get)
print("Resultado más frecuente:", most_frequent_result, "con", counts[most_frequent_result], "apariciones")

