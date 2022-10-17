from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# Apply gates to set qubit in superposition
# Such that 60% is head (ie 0), and 40% is tails (ie 1)

# Derivation of angle 1.369:
# Using https://quantumcomputing.stackexchange.com/questions/9282/what-is-the-corresponding-code-for-finding-the-state-of-a-qubit-on-the-bloch-sph
# First of all, we need to find the final matrix coefficients. for state 0.6 probability of state 0, and 0.4 of 1, let us assume the coeff. by a and b
# ie the qubit in state q = a|0> + b|1>, thf. we know that 0.6 = a^2/(a^2+b^2), => a = √(3/2), b = 1. Now we know the final qubit matrix coefficients,
# We just need to find the angle for ry gate for which we can convert the matrix to this state!
# Ie using ```Ry(θ) will transform the qubit from the |0⟩ state to |ψ⟩=cosθ2|0⟩+sinθ2|1⟩,```, Using cos^2(θ) + sin^2(θ) = 1 and finding theta for this case
# We get θ=1.369

# If you cannot understand the above derivation then a handwritten derivation is also there in handwritten_soln.pdf

qc.ry(1.369, 0)
qc.measure(0,0)

# Draw circuit
print(qc.draw(output='text'))

# Simulate, or toss coins!
backend = Aer.get_backend("statevector_simulator")
job = backend.run(qc, shots=100)
result = job.result()

# Show results :)
plot_histogram(result.get_counts())
plt.show()