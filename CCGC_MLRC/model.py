import torch
import torch.nn as nn
import torch.nn.functional as F
from layers import *
from torch.nn import Linear
from torch_geometric.nn import GATConv, GCNConv, ChebConv
from torch_geometric.nn import JumpingKnowledge
from torch_geometric.nn import MessagePassing, APPNP


class Encoder_Net(nn.Module):
    def __init__(self, layers, dims):
        super(Encoder_Net, self).__init__()

        # self.shared_layer = nn.Linear(dims[0], dims[1])
        self.layers1 = nn.Linear(dims[0], dims[1])
        self.layers2 = nn.Linear(dims[0], dims[1])
        # self.layers1 = self.shared_layer
        # self.layers2 = self.shared_layer

    def forward(self, x):
        out1 = self.layers1(x)
        out2 = self.layers1(x)

        out1 = F.normalize(out1, dim=1, p=2)
        out2 = F.normalize(out2, dim=1, p=2)

        # print("out1", out1," ", "out2",out1)

        return out1, out2

