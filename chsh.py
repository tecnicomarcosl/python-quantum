# Importaciones requeridas

from qiskit import QuantumCircuit
from qiskit_aer.primitives import Sampler
from numpy import pi
from numpy.random import randint

def juego_chsh(estrategia):
    """Juega el juego CHSH
    Args:
        estrategia: Una función que toma dos bits (como `int`s) y
            devuelve dos bits (también como `int`s). La estrategia debe seguir
            las reglas del juego CHSH.
    Returns:
        int: 1 para una victoria, 0 para una derrota.
    """
    # El árbitro elige x e y aleatoriamente
    x, y = randint(0, 2), randint(0, 2)

    # Usa la estrategia para elegir a y b
    a, b = estrategia(x, y)

    # El árbitro decide si Alice y Bob ganan o pierden
    if (a != b) == (x & y):
        return 1  # Victoria
    return 0  # Derrota

def circuito_chsh(x, y):
    """Crea un `QuantumCircuit` que implementa la mejor estrategia CHSH.
    Args:
        x (int): El bit de Alice (debe ser 0 o 1)
        y (int): El bit de Bob (debe ser 0 o 1)
    Returns:
        QuantumCircuit: Circuito que, cuando se ejecute, devuelve los bits de
            respuesta de Alice y Bob.
    """
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()

    # Alice
    if x == 0:
        qc.ry(0, 0)
    else:
        qc.ry(-pi / 2, 0)
    qc.measure(0, 0)

    # Bob
    if y == 0:
        qc.ry(-pi / 4, 1)
    else:
        qc.ry(pi / 4, 1)
    qc.measure(1, 1)

    return qc

# Dibuja los cuatro circuitos posibles

print("(x,y) = (0,0)")
display(circuito_chsh(0, 0).draw())

print("(x,y) = (0,1)")
display(circuito_chsh(0, 1).draw())

print("(x,y) = (1,0)")
display(circuito_chsh(1, 0).draw())

print("(x,y) = (1,1)")
display(circuito_chsh(1, 1).draw())

muestreador = Sampler()

def estrategia_cuantica(x, y):
    """Realiza la mejor estrategia para el juego CHSH.
    Args:
        x (int): El bit de Alice (debe ser 0 o 1)
        y (int): El bit de Bob (debe ser 0 o 1)
    Returns:
        (int, int): Los bits de respuesta de Alice y Bob (respectivamente)
    """
    # `shots=1` ejecuta el circuito una vez
    resultado = muestreador.run(circuito_chsh(x, y), shots=1).result()
    estadisticas = resultado.quasi_dists[0].binary_probabilities()
    bits = list(estadisticas.keys())[0]
    a, b = bits[0], bits[1]
    return a, b

NUM_JUEGOS = 1000
PUNTAJE_TOTAL = 0

for _ in range(NUM_JUEGOS):
    PUNTAJE_TOTAL += juego_chsh(estrategia_cuantica)

print("Fracción de juegos ganados:", PUNTAJE_TOTAL / NUM_JUEGOS)

def estrategia_clasica(x, y):
    """Una estrategia clásica óptima para el juego CHSH
    Args:
        x (int): El bit de Alice (debe ser 0 o 1)
        y (int): El bit de Bob (debe ser 0 o 1)
    Returns:
        (int, int): Los bits de respuesta de Alice y Bob (respectivamente)
    """
    # Respuesta de Alice
    if x == 0:
        a = 0
    elif x == 1:
        a = 1

    # Respuesta de Bob
    if y == 0:
        b = 1
    elif y == 1:
        b = 0

    return a, b

NUM_JUEGOS = 1000
PUNTAJE_TOTAL = 0

for _ in range(NUM_JUEGOS):
    PUNTAJE_TOTAL += juego_chsh(estrategia_clasica)

print("Fracción de juegos ganados:", PUNTAJE_TOTAL / NUM_JUEGOS)
