""" EdMot clustering class."""

import community
import networkx as nx
from tqdm import tqdm

class EdMot(object):
    """
    Edge Motif Clustering Class.
    """
    def __init__(self, graph, component_count, cutoff):
        """
        :param graph: NetworkX object.
        :param component_count: Number of extract motif hypergraph components.
        :param cutoff: Motif edge cut-off value.
        """
        self.graph = graph
        self.component_count = component_count
        self.cutoff = cutoff

    def _overlap(self, node_1, node_2):
        """
        Calculating the neighbourhood overlap for a pair of nodes.
        :param node_1: Source node 1.
        :param node_2: Source node 2.
        :return neighbourhood overlap: Overlap score.
        """
        nodes_1 = self.graph.neighbors(node_1)
        nodes_2 = self.graph.neighbors(node_2)

        return len(set(nodes_1).intersection(set(nodes_2)))

    def _calculate_motifs(self):
        """
        Enumerating pairwise motif counts.
        """
        print("\nCalculating overlaps.\n")
        edges = [e for e in tqdm(self.graph.edges()) if self._overlap(e[0], e[1]) >= self.cutoff]
        self.motif_graph = nx.from_edgelist(edges)

    def _extract_components(self):
        """
        Extracting connected components from motif graph.
        """
        print("\nExtracting components.")
        components = [c for c in nx.connected_components(self.motif_graph)]
        components = [[len(c), c] for c in components]
        components.sort(key=lambda x: x[0], reverse=True)
        important_components = [components[comp][1] for comp
                                in range(self.component_count if len(components)>=self.component_count else len(components))]
        self.blocks = [list(graph) for graph in important_components]

        print("Found %d blocks." % len(self.blocks))
        print("Block sizes: %s" % ', '.join(str(len(block)) for block in self.blocks))

    def _extract_mods(self):
        """
        Extracting mods in the top-K connected components.
        """
        self.mods = []
        print('\nAnalyzing mods.')
        for block in tqdm(self.blocks):
            temp_mods = {}
            block = self.motif_graph.subgraph(block).copy()
            temp_partition = community.best_partition(block)
            for node, part in temp_partition.items():
                if part not in temp_mods.keys():
                    temp_mods[part] = [node,]
                else:
                    temp_mods[part].append(node)
            self.mods.extend(temp_mods.values())
        print('Found %d motifs.' % len(self.mods))
        print('Motif sizes: %s' % ', '.join(str(len(mod)) for mod in self.mods))

    def _fill_blocks(self):
        """
        Filling the dense blocks of the adjacency matrix.
        """
        print("Adding edge blocks.\n")
        for nodes in tqdm(self.blocks):
            new_edges = [(n_1, n_2) for n_1 in nodes for n_2 in nodes if n_1!= n_2]
            self.graph.add_edges_from(new_edges)

    def fit(self):
        """
        Clustering the target graph.
        """
        self._calculate_motifs()
        self._extract_components()
        self._extract_mods()
        self._fill_blocks()
        partition = community.best_partition(self.graph)
        return partition
