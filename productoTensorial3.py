import numpy as np
from sympy import Rational

# Definimos las matrices A, B, C y D
A = np.array([[1, 1/2],
              [0, 1/2]])

B = np.array([[0, 1],
              [1, 0]])

C = np.array([[1, 0],
              [1, 0]])

D = np.array([[0, 1/2],
              [1, np.sqrt(2)]])

# Calculamos el producto de A y B
E = np.dot(A, B)
F = np.dot(C, D)

print("El producto de A y B es:")
print(E)
print(np.vectorize(Rational)(E))

print("El producto de C y D es:")
print(np.vectorize(Rational)(F))

# Calculamos el producto tensorial de E y F
G = np.kron(E, F)

print("El producto tensorial de E y F es:")
print(np.vectorize(Rational)(G))

# Calculamos el producto tensorial de A y B y de C y D
H = np.kron(A, C)
I = np.kron(B, D)

print("El producto Tensorial de A y B es:")
print(np.vectorize(Rational)(H))
print("El producto Tensorial de C y D es:")
print(np.vectorize(Rational)(I))

J = np.dot(H, I)
print("El producto de H e I es:")
print(np.vectorize(Rational)(J))

# Comparamos los resultados G y J
if np.array_equal(G, J):
    print("Los resultados G y J son iguales.")
else:
    print("Los resultados G y J son diferentes.")
