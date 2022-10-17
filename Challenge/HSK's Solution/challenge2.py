from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create quantum circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# Put it in state 1, or apply X gate to |0>
qc.x(0)

# Put it into equal superposition now, ie apply hadmard gate on |1>, which will become |->, Mathematics shown in handwritten_soln.pdf
qc.h(0)

# Measure circuit
qc.measure(0,0)

# Draw circuit
print(qc.draw(output='text'))

# Simulate!
backend = Aer.get_backend("statevector_simulator")
job = backend.run(qc, shots=100)
result = job.result()

# Show results :)
plot_histogram(result.get_counts())
plt.show()