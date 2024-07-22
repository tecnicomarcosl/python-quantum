from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector
from IPython.display import display

# Creamos un circuito cuántico con 1 qubit
qc = QuantumCircuit(1)

# Seleccionamos el simulador Aer
backend = Aer.get_backend('statevector_simulator')

# Bucle para aplicar las compuertas hasta que el usuario decida salir
while True:
    # Preguntar al usuario qué compuerta desea aplicar
    compuerta = input("Elija una compuerta (X, Y, Z, H) o escriba 'Salir' para salir: ").upper()
    
    # Verificar si el usuario quiere salir
    if compuerta == 'SALIR':
        break
    
    # Verificar la entrada del usuario y aplicar la compuerta correspondiente
    if compuerta == 'X':
        qc.x(0)
        result = backend.run(qc).result()
        statevector = result.get_statevector()
        print(f"Después de aplicar la compuerta {compuerta}:")
        print("Estado vectorial:", statevector)
        display(plot_bloch_multivector(statevector))
    elif compuerta == 'Y':
        qc.y(0)
        result = backend.run(qc).result()
        statevector = result.get_statevector()
        print(f"Después de aplicar la compuerta {compuerta}:")
        print("Estado vectorial:", statevector)
        display(plot_bloch_multivector(statevector))
    elif compuerta == 'Z':
        qc.z(0)
        result = backend.run(qc).result()
        statevector = result.get_statevector()
        print(f"Después de aplicar la compuerta {compuerta}:")
        print("Estado vectorial:", statevector)
        display(plot_bloch_multivector(statevector))
    elif compuerta == 'H':
        qc.h(0)
        result = backend.run(qc).result()
        statevector = result.get_statevector()
        print(f"Después de aplicar la compuerta {compuerta}:")
        print("Estado vectorial:", statevector)
        display(plot_bloch_multivector(statevector))
    else:
        print("Compuerta no válida.")
