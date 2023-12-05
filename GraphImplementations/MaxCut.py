import networkx as nx
import pyomo.core as pyo
from IPython.display import Markdown, display

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

from classiq import construct_combinatorial_optimization_model
from classiq.applications.combinatorial_optimization import OptimizerConfig, QAOAConfig


def arithmetic_eq(x1: int, x2: int) -> int:
    return x1 * (1 - x2) + x2 * (1 - x1)



def maxcut(graph: nx.Graph) -> pyo.ConcreteModel:
    model = pyo.ConcreteModel()
    model.x = pyo.Var(graph.nodes, domain=pyo.Binary)
    model.cost = pyo.Objective(
        expr=sum(
            arithmetic_eq(model.x[node1], model.x[node2])
            for (node1, node2) in graph.edges
        ),
        sense=pyo.maximize,
    )
    return model


G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4])
G.add_edges_from([(0, 1), (0, 2), (1, 2), (1, 3), (2, 4), (3, 4)])
pos = nx.planar_layout(G)
nx.draw_networkx(G, pos=pos, with_labels=True, alpha=0.8, node_size=500)
plt.show()
max_cut_model = maxcut(G)

qaoa_config = QAOAConfig(num_layers=4)
optimizer_config = OptimizerConfig(max_iteration=60, alpha_cvar=0.7)

qmod = construct_combinatorial_optimization_model(
    pyo_model=max_cut_model,
    qaoa_config=qaoa_config,
    optimizer_config=optimizer_config,
)

with open("max_cut.qmod", "w") as f:
    f.write(qmod)