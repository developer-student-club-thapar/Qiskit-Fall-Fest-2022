from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# quantum circuit is created with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# Appling gates to set qubit in superposition such that 40% is tails (which is 1) and 60% is head (which is 0).

# Derivation of angle 1.863:
# Using https://quantumcomputing.stackexchange.com/questions/9282/what-is-the-corresponding-code-for-finding-the-state-of-a-qubit-on-the-bloch-sph
# At first, we find the final matrix coefficients. for state 0.6 probability of state 0, and 0.4 of 1, let us assume the coefficient by x and y that is the qubit in state q = x|0> + y|1>, therefore, we know that 0.6 = x^2/(x^2+y^2), =>x = √(3/2), y = 1. Now we know the final qubit matrix coefficients,
# We just need to find the angle for ry gate for which we can convert the matrix to this state!
# that is by  using ```Ry(θ) it will transform the qubit from the |0⟩ state to |ψ⟩=cosθ2|0⟩+sinθ2|1⟩,```, Using cos^2(θ) + sin^2(θ) = 1 and finding theta for this case
# We get θ=1.369

qc.ry(1.863, 0)
qc.measure(0,0)

# Circuit
print(qc.draw(output='text'))

# Simulate or toss coins
backend = Aer.get_backend("statevector_simulator")
job = backend.run(qc, shots=100)
result = job.result()

# Results
plot_histogram(result.get_counts())
plt.show()