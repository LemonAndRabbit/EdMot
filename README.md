EdMot
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/mixhop-higher-order-graph-convolution/node-classification-on-citeseer)](https://paperswithcode.com/sota/node-classification-on-citeseer?p=mixhop-higher-order-graph-convolution)
![GitHub stars](https://img.shields.io/github/stars/benedekrozemberczki/EdMot.svg?style=plastic)
![GitHub forks](https://img.shields.io/github/forks/benedekrozemberczki/EdMot.svg?color=blue&style=plastic)
![License](https://img.shields.io/github/license/benedekrozemberczki/EdMot.svg?color=blue&style=plastic)
============================================
A NetworkX implementation of "EdMot: An Edge Enhancement Approach for Motif-aware Community Detection" (KDD 2019).
<p align="center">
  <img width="800" src="mixhop1.jpg">
</p>

### Abstract

<p align="justify">
Network community detection is a hot research topic in network analysis. Although many methods have been proposed for community detection, most of them only take into consideration the lower-order structure of the network at the level of individual nodes and edges. Thus, they fail to capture the higher-order characteristics at the level of small dense subgraph patterns, e.g., motifs. Recently, some higher-order methods have been developed but they typically focus on the motif-based hypergraph which is assumed to be a connected graph. However, such assumption cannot be ensured in some real-world networks. In particular, the hypergraph may become fragmented. That is, it may consist of a large number of connected components and isolated nodes, despite the fact that the original network is a connected graph. Therefore, the existing higher-order methods would suffer seriously from the above fragmentation issue, since in these approaches, nodes without connection in hypergraph can't be grouped together even if they belong to the same community. To address the above fragmentation issue, we propose an Edge enhancement approach for Motif-aware community detection (EdMot ). The main idea is as follows. Firstly, a motif-based hypergraph is constructed and the top K largest connected components in the hypergraph are partitioned into modules. Afterwards, the connectivity structure within each module is strengthened by constructing an edge set to derive a clique from each module. Based on the new edge set, the original connectivity structure of the input network is enhanced to generate a rewired network, whereby the motif-based higher-order structure is leveraged and the hypergraph fragmentation issue is well addressed. Finally, the rewired network is partitioned to obtain the higher-order community structure. Extensive experiments have been conducted on eight real-world datasets and the results show the effectiveness of the proposed method in improving the community detection performance of state-of-the-art methods.</p>

This repository provides a PyTorch implementation of EdMot as described in the papers:

> MixHop: Higher-Order Graph Convolutional Architectures via Sparsified Neighborhood Mixing
> Pei-Zhen Li, Ling Huang, Chang-Dong Wang, and  Jian-Huang Lai .
> KDD, 2019.
> [[Paper]](https://arxiv.org/pdf/1905.00067.pdf)

A Matlab implementation of EdMot is available [[here]](https://github.com/samihaija/mixhop).

### Requirements
The codebase is implemented in Python 3.5.2. package versions used for development are just below.
```
networkx          1.11
tqdm              4.28.1
numpy             1.15.4
pandas            0.23.4
texttable         1.5.0
scipy             1.1.0
argparse          1.1.0
torch             0.4.1
torch-sparse      0.2.2
```
### Datasets

The code takes the **edge list** of the graph in a csv file. Every row indicates an edge between two nodes separated by a comma. The first row is a header. Nodes should be indexed starting with 0. A sample graph for `Cora` is included in the  `input/` directory. In addition to the edgelist there is a JSON file with the sparse features and a csv with the target variable.


### Options
Training an N-GCN/MixHop model is handled by the `src/main.py` script which provides the following command line arguments.

#### Input and output options
```
  --edge-path       STR    Edge list csv.         Default is `input/cora_edges.csv`.
  --features-path   STR    Features json.         Default is `input/cora_features.json`.
```
#### Model options
```
  --model             STR     Model variant.                 Default is `mixhop`.               
  --seed              INT     Random seed.                   Default is 42.
  --epochs            INT     Number of training epochs.     Default is 2000.
  --early-stopping    INT     Early stopping rounds.         Default is 10.
  --training-size     INT     Training set size.             Default is 1500.
  --validation-size   INT     Validation set size.           Default is 500.
  --learning-rate     FLOAT   Adam learning rate.            Default is 0.01.
  --dropout           FLOAT   Dropout rate value.            Default is 0.5.
  --lambd             FLOAT   Regularization coefficient.    Default is 0.0005.
  --layers-1          LST     Layer sizes (upstream).        Default is [200, 200, 200]. 
  --layers-2          LST     Layer sizes (bottom).          Default is [200, 200, 200].
  --cut-off           FLOAT   Norm cut-off for pruning.      Default is 0.1.
  --budget            INT     Architecture neuron budget.    Default is 60.
```
### Examples
The following commands learn a neural network and score on the test set. Training a model on the default dataset.
```
python src/main.py
```
<p align="center">
<img style="float: center;" src="mixhop.gif">
</p>

Training a MixHop model for a 100 epochs.
```
python src/main.py --epochs 100
```
Increasing the learning rate and the dropout.
```
python src/main.py --learning-rate 0.1 --dropout 0.9
```
Training a model with diffusion order 2:
```
python src/main.py --layers 64 64
```
Training an N-GCN model:
```
python src/main.py --model ngcn
```
