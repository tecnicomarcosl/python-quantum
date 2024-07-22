from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

# Creamos un circuito cuántico con un solo qubit
qc = QuantumCircuit(2)

# Aplicamos una compuerta Hadamard para poner el qubit en una superposición

#qc.h(0)
#qc.h(1)

# Aplicamos una compuerta CNOT con el primer qubit como control y el segundo como objetivo
qc.cx(0, 1)

# Medimos el qubit
qc.measure_all()

# Transpilamos el circuito para adaptarlo al backend
new_circuit = transpile(qc, Aer.get_backend('qasm_simulator'))

# Ejecutamos el circuito en el backend
backend = Aer.get_backend('qasm_simulator')
job = backend.run(new_circuit, shots=1000)

# Obtenemos el resultado de la ejecución
result = job.result()
counts = result.get_counts()

# Obtenemos el resultado de la medición (resultado aleatorio)
random_result = list(counts.keys())[0]

print("Resultado de la medición:", random_result)
