"""Utils for evaluation"""

import json
import readline

def read_partition(partition_path):
    """"Load Membership file as a python dict object: community label -> community nodes."""
    partition = {}
    with open(partition_path, "r") as f:
        nodes = json.load(f)
        for node, label in nodes.items():
            if label not in partition.keys():
                partition[label] = [int(node),]
            else:
                partition[label].append(int(node))

    return partition

class Target:
    """A class that represent target communities
    
    Attributes:
        label: A dict that maps node indice to its target community.
        communities: A dict that maps community name to its member count.
    """

    def __init__(self, target_path):
        self.label = {}
        self.communities = {}
        self.len = 0
        with open(target_path, "r") as f:
            f.readline()
            lines = f.readlines()
            for line in lines:
                pair = line.split(',')
                self.label[int(pair[0])] = int(pair[1])
                self.communities[int(pair[1])] = self.communities.get(int(pair[1]), 0) + 1
                self.len += 1

    def __len__(self):
        """Returns total node count."""
        return self.len

