import numpy as np
import matplotlib.pyplot as plt
import qiskit


# makes a binary tree of required depth for Testing
def generate_binary_graph(depth):
    graph = {}
    # add all non-leaves
    for i in range(1, depth):
        current_nodes = range(2**(i-1), 2**i)
        first_child_node = 2**i
        for node in current_nodes:
            graph[node] = [first_child_node, first_child_node + 1]
            first_child_node += 2
    # add all leaves
    for i in range(2**(depth-1), 2**depth):
        graph[i] = []
    return graph


# generates the diffusion operator Dx as defined by Montanaro for marked, root and normal nodes.
def generate_diffusion_operator(node, graph, depth, marked_node):
    D = np.identity(2**depth)
    psi = np.zeros(2 ** depth)
    root_node = 1
    if node == marked_node:
        return psi, D
    elif node == root_node:
        # add root node
        psi[node] = 1
        d = len(graph[root_node])
        for child_node in graph[node]:
            psi[child_node] += np.sqrt(depth)
        # scale
        psi = psi / np.sqrt(1 + d*depth)
        # calculate D
        D = D - 2 * np.outer(psi, psi)
        return psi, D
    else:
        # add current node
        psi[node] = 1
        d = len(graph[node]) + 1
        for child_node in graph[node]:
            psi[child_node] += 1
        # scale
        psi = psi / np.sqrt(d)
        # calculate D
        D = np.identity(2**depth) - 2 * np.outer(psi, psi)
        return psi, D


def validator(psi, D):
    s = sum([x**2 for x in psi])
    print("psi_length: ", s)
    print("Determinant of D: ", np.linalg.det(D))


Depth = 4
Graph = generate_binary_graph(Depth)
print(Graph)

Psi, Diffuser = generate_diffusion_operator(node=5, graph=Graph, depth=Depth, marked_node=5)
validator(psi=Psi, D=Diffuser)





