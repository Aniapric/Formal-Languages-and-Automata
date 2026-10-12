import networkx as nx  # Standard Python library for graph creation and analysis

def is_power_of_two(n):
    """
    Ignore cycle lengths smaller than 4.
    Since we convert the graph to directed (to use nx.simple_cycles),
    edges become bidirectional (A->B and B->A).
    This creates trivial false cycles of length 2.
    If we don't filter out length 2, the program would report false positives.
    """
    if n < 4:
        return False
    while n > 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True

def has_power_of_two_cycle(G):
    """
    nx.simple_cycles finds elementary cycles (no repeated nodes) in a graph.
    Since simple_cycles only works on directed graphs, we use to_directed()
    to convert the undirected cubic graph into a directed graph.
    """
    cycles = nx.simple_cycles(G.to_directed())
    for cycle in cycles:
        # Check the length of each simple cycle found
        if is_power_of_two(len(cycle)):
            return True, len(cycle)  # Stop at first valid power-of-two cycle found
    return False, None

def run_experiment(num_graphs, num_nodes):
    """
    Run the empirical verification of the Erdős–Gyárfás conjecture
    on random 3-regular (cubic) graphs.
    """
    satisfied = 0

    for i in range(num_graphs):
        # nx.random_regular_graph generates a 3-regular graph (each vertex has degree 3),
        # matching the hypothesis of the conjecture.
        G = nx.random_regular_graph(3, num_nodes)
        found, length = has_power_of_two_cycle(G)

        if found:
            satisfied += 1
            print(f"Graph {i + 1}: YES - cycle of length {length}")
        else:
            print(f"Graph {i + 1}: NO - potential counterexample!")

    print(f"\nSatisfying the conjecture: {satisfied} out of {num_graphs}")

# Aliases for backwards compatibility
este_putere_de_2 = is_power_of_two
are_ciclu_putere_de_2 = has_power_of_two_cycle
ruleaza_experiment = run_experiment

if __name__ == "__main__":
    # Run experiment on 200 random 3-regular graphs with 16 nodes each
    run_experiment(200, 16)
