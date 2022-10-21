from turtle import back
from qiskit import QuantumCircuit, ClassicalRegister, assemble, Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

def showresult(circ):
    # simulate
    backend = Aer.get_backend("statevector_simulator")
    job = backend.run(bs1, shots=100)
    result = job.result()

    # results
    plot_histogram(result.get_counts())
    plt.show()

# here we create 4 entangled bell states using 2 qubit. ref. https://quantumcomputinguk.org/tutorials/introduction-to-bell-states

# Bellstate 1
# Creating quantum circuit with 2 qubit and 2 classical bit
bs1 = QuantumCircuit(2,2)
# it is put in state 1 or X gate is applied to |0>
bs1.h(0)
# it is put into equal superposition now, that is hadmard gate is applied on |1>, which becomes |->
bs1.cnot(0,1)
# measure circuit
bs1.measure([0,1],[0,1])
# draw circuit
print(bs1.draw(output='text'))
# showresult(bs1)

# Bellstate 2
# Creating quantum circuit with 2 qubit and 2 classical bit
bs2 = QuantumCircuit(2,2)
bs2.x(0)
# it is put in state 1 or X gate is applied to |0>
bs2.h(0)
# it is put into equal superposition now, that is hadmard gate is applied on |1>, which becomes |->
bs2.cnot(0,1)
# measure circuit
bs2.measure([0,1],[0,1])
# draw circuit
print(bs2.draw(output='text'))
# showresult(bs2)

# Bellstate 3
# Creating quantum circuit with 2 qubit and 2 classical bit
bs2 = QuantumCircuit(2,2)
bs2.x(1)
# it is put in state 1 or X gate is applied to |0>
bs2.h(0)
# it is put into equal superposition now, that is hadmard gate is applied on |1>, which becomes |->
bs2.cnot(0,1)
# measure circuit
bs2.measure([0,1],[0,1])
# draw circuit
print(bs2.draw(output='text'))
# showresult(bs3)

# Bellstate 4
# Creating quantum circuit with 2 qubit and 2 classical bit
bs4 = QuantumCircuit(2,2)
bs4.x(1)
# Put it in state 1, or apply X gate to |0>
bs4.h(0)

bs4.z(0)
bs4.z(1)

# it is put into equal superposition now, that is hadmard gate is applied on |1>, which becomes |->
bs4.cnot(0,1)
# measure circuit
bs4.measure([0,1],[0,1])
# draw circuit
print(bs4.draw(output='text'))
# showresult(bs4)