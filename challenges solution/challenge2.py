from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# quantum circuit is created with 1 qubit and 1 classical bit
qc = QuantumCircuit(1,1)

# it is put in state 1 or X gate is applied to |0>
qc.x(0)

# it is now put into equal superposition, that is apply hadmard gate on |1>, which becomes |->
qc.h(0)

# measure circuit
qc.measure(0,0)

# draw circuit
print(qc.draw(output='text'))

# simulate
backend = Aer.get_backend("statevector_simulator")
job = backend.run(qc, shots=100)
result = job.result()

# results 
plot_histogram(result.get_counts())
plt.show()