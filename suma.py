from qiskit import QuantumCircuit, transpile, assemble
from qiskit_aer import AerSimulator

# Función para crear un circuito cuántico para sumar dos números clásicos
def circuito_suma(a, b):
    # Crea un circuito cuántico con 4 qubits (2 para los números y 2 para el resultado)
    circuito = QuantumCircuit(4, 2)

    # Codifica los números en los primeros dos qubits (a en el primer qubit y b en el segundo qubit)
    if a:
        circuito.x(0)  # Aplica una puerta X al primer qubit si 'a' es 1
    if b:
        circuito.x(1)  # Aplica una puerta X al segundo qubit si 'b' es 1

    # Suma los dos números clásicos utilizando un circuito cuántico
    circuito.ccx(0, 1, 3)  # Puerta Toffoli: Suma 'a' y 'b', almacena el resultado en el tercer qubit
    circuito.cx(0, 1)      # Puerta CNOT: Suma 'a' y 'b', almacena el resultado en el segundo qubit

    # Mide los qubits y almacena el resultado en los bits clásicos
    circuito.measure([1, 3], [0, 1])

    return circuito

# Ejemplo de suma de números (a=1, b=1)
if __name__ == "__main__":
    a = 0
    b = 1

    # Crea el circuito cuántico para sumar los números dados
    mi_circuito = circuito_suma(a, b)

    # Transpila el circuito para el simulador QASM
    simulador = AerSimulator()
    circuito_transpilado = transpile(mi_circuito, simulador)

    # Ensambla el circuito transpilado en un objeto Qobj
    qobj = assemble(circuito_transpilado)

    # Ejecuta el circuito en el simulador y obtén los resultados
    resultado = simulador.run(circuito_transpilado).result()

    # Imprime los resultados de la ejecución
    conteos = resultado.get_counts()
    print("Resultados de la ejecución cuántica:", conteos)
