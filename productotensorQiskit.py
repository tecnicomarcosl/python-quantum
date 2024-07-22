from qiskit.quantum_info import Statevector, Operator
from numpy import sqrt

# We create two state vectors representing |0⟩ and |1⟩
zero, one = Statevector.from_label("0"), Statevector.from_label("1")

#and use the tensor method to create a new vector, ∣0⟩ ⊗ ∣1⟩
display(zero.tensor(one).draw("latex"))

# We create state vectors representing |+⟩ and 1/sqrt(2)(|0⟩+i|1⟩)
plus = Statevector.from_label("+")
i_state = Statevector([1 / sqrt(2), 1j / sqrt(2)])
psi = plus.tensor(i_state)

display(psi.draw("latex"))

X = Operator([[0, 1], [1, 0]])
I = Operator([[1, 0], [0, 1]])

print(X.tensor(I))

display(psi.evolve(I ^ X).draw("latex"))

CX = Operator(
    [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 1, 0],
    ]
)

display(psi.evolve(CX).draw("latex"))