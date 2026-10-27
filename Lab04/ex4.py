from pgmpy.models import DiscreteMarkovNetwork
import networkx as nx
model = DiscreteMarkovNetwork()

model.add_edges_from([
    ("A1", "A2"),
    ("A1", "A3"),
    ("A2", "A4"),
    ("A2", "A5"),
    ("A3", "A4"),
    ("A4", "A5")
])


cliques = list(nx.find_cliques(model))

print("Clicile maximale:")
print(cliques)