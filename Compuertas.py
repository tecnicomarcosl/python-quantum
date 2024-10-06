import numpy as np

# Definir los qubits como vectores columna
q0 = np.array([[1], 
                [0]]) 

q1 = np.array([[1], 
                [0]]) 

# Producto tensorial para formar el estado del sistema de 2 qubits
sist2qubit = np.kron(q0, q1)
print('')
print(sist2qubit)

# Definimos la matriz I
I = np.array([[1, 0],
              [0, 1]])

# Definimos la matriz X
X = np.array([[0, 1],
            [1, 0]])

# Definimos la matriz Y
Y = np.array([[0, -1j],
              [1j, 0]])

# Definimos la matriz Z
Z = np.array([[1, 0],
              [0, -1]])

# Definimos la matriz H
H = (1/np.sqrt(2)) * np.array([[1, 1],
                                [1, -1]])


# Definimos la matriz S
# La puerta S es una puerta de fase que aplica una fase de π/2​ (90 grados) al 
# estado ∣1⟩ de un solo qubit, sin afectar el estado ∣0⟩
S = np.array([[1, 0],
              [0, 1j]])

# Definimos la matriz CNOT
CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]])

# Definimos la matriz CZ
# La puerta de fase controlada aplica una fase a un qubit objetivo dependiendo 
# del estado de un qubit de control. Por ejemplo, la puerta Controlled-Z (CZ) 
# aplica una fase de π al qubit objetivo solo cuando el qubit de control está 
# en ∣1⟩:

CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]])

# Definimos la matriz T
# La puerta T es una compuerta de fase que aplica una rotación de fase de π/4
#​ (45 grados) al estado ∣1⟩ de un qubit, mientras que deja el estado ∣0⟩ 
# sin cambios

T = np.array([[1, 0],
              [0, np.exp(1j * np.pi / 4)]])


# Definimos la función para la matriz R(theta) en grados
# La puerta R(θ) realiza una rotación al alrededor del 
# eje z por el ángulo θ que le indiques
def R(theta_degrees):
    theta = np.radians(theta_degrees)  # Convertir a radianes
    return np.array([[np.exp(-1j * theta / 2), 0],
                     [0, np.exp(1j * theta / 2)]])

# Ejemplo de uso
#theta = 90  # Rotación de 90 grados
#R_theta = R(theta)


# Definimos la función para la matriz RX(theta)
# La puerta RX(θ) realiza una rotación al alrededor del 
# eje x por el ángulo θ que le indiques
def RX(theta_degrees):
    theta = np.radians(theta_degrees)  # Convertir a radianes
    return np.array([[np.cos(theta / 2), -1j * np.sin(theta / 2)],
                     [-1j * np.sin(theta / 2), np.cos(theta / 2)]])

# Ejemplo de uso
#theta_x = 90  # Rotación de 90 grados
#RX_theta = RX(theta_x)  

# Definimos la función para la matriz RY(theta)
# La puerta R(θ) realiza una rotación al alrededor del 
# eje y por el ángulo θ que le indiques
def RY(theta_degrees):
    theta = np.radians(theta_degrees)  # Convertir a radianes
    return np.array([[np.cos(theta / 2), -np.sin(theta / 2)],
                     [np.sin(theta / 2), np.cos(theta / 2)]])

# Ejemplo de uso
#theta_y = 90  # Rotación de 90 grados
#RY_theta = RY(theta_y)


# Producto tensorial para formar una compuerta X al primer qubit y nada al segundo
gateXI = np.kron(I, X)

#print(produc)
print('')
print(gateXI)


# Producto punto para aplicar la compurta a los 2 qubits
resultado=np.dot(gateXI,sist2qubit)
print('')
print(resultado)