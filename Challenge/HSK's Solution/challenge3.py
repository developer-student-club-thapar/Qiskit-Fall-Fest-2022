from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def showresult(circ):
    # Simulate!
    backend = Aer.get_backend("statevector_simulator")
    job = backend.run(bs1, shots=100)
    result = job.result()

    # Show results :)
    plot_histogram(result.get_counts())
    plt.show()

# Here we can create 4 entangled bell states using 2 qubit! ref. https://quantumcomputinguk.org/tutorials/introduction-to-bell-states

# Bellstate 1
# Create quantum circuit with 2 qubit and 2 classical bit
bs1 = QuantumCircuit(2,2)
# Put it in state 1, or apply X gate to |0>
bs1.h(0)
# Put it into equal superposition now, ie apply hadmard gate on |1>, which will become |->, Mathematics shown in handwritten_soln.pdf
bs1.cnot(0,1)
# Measure circuit
bs1.measure([0,1],[0,1])
# Draw circuit
print(bs1.draw(output='text'))
# showresult(bs1)


# Bellstate 2
# Create quantum circuit with 2 qubit and 2 classical bit
bs2 = QuantumCircuit(2,2)
bs2.x(0)
# Put it in state 1, or apply X gate to |0>
bs2.h(0)
# Put it into equal superposition now, ie apply hadmard gate on |1>, which will become |->, Mathematics shown in handwritten_soln.pdf
bs2.cnot(0,1)
# Measure circuit
bs2.measure([0,1],[0,1])
# Draw circuit
print(bs2.draw(output='text'))
# showresult(bs2)


# Bellstate 3
# Create quantum circuit with 2 qubit and 2 classical bit
bs2 = QuantumCircuit(2,2)
bs2.x(1)
# Put it in state 1, or apply X gate to |0>
bs2.h(0)
# Put it into equal superposition now, ie apply hadmard gate on |1>, which will become |->, Mathematics shown in handwritten_soln.pdf
bs2.cnot(0,1)
# Measure circuit
bs2.measure([0,1],[0,1])
# Draw circuit
print(bs2.draw(output='text'))
# showresult(bs3)

# Bellstate 4
# Create quantum circuit with 2 qubit and 2 classical bit
bs4 = QuantumCircuit(2,2)
bs4.x(1)
# Put it in state 1, or apply X gate to |0>
bs4.h(0)

bs4.z(0)
bs4.z(1)

# Put it into equal superposition now, ie apply hadmard gate on |1>, which will become |->, Mathematics shown in handwritten_soln.pdf
bs4.cnot(0,1)
# Measure circuit
bs4.measure([0,1],[0,1])
# Draw circuit
print(bs4.draw(output='text'))
# showresult(bs4)