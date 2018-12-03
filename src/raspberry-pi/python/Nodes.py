from math import sqrt
class Node:
    def __init__(self, Name, Position):
        self.Name = Name
        self.Connections = {}
        self.Position = Position



Node1 = Node(Name="Node 1", Position= (1,1))
Node2 = Node(Name= "Node 2", Position=(0,0))
Node3 = Node(Name = "Node 3")
Node4 = Node(Name = "Node 4")

def NextTo(Node, NextNode):
    Weight = sqrt((((Node.Position[0] - NextNode.Position[0])^2) + (Node.Position[1] - NextNode.Position[1])^2))
    Node.Connections[NextNode] = Weight
    NextNode.Connections[Node] = Weight
    return Node

NextTo(Node1, Node2, 2)
NextTo(Node1, Node3, 3)
NextTo(Node2, Node4, 5)
NextTo(Node3, Node4, 1)


print(Node1.Connections)








