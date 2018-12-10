#Imports, math for sqrt and time for debugging purposes
from math import sqrt
import time


#The node class which allows us to navigate and place points on a plane
class Node:
    def __init__(self, Name, Position):
        self.Name = Name
        self.Connections = {}
        self.Position = Position

#Our way of generating the connection between nodes and the "weight" connecting them
def NextTo(Node, NextNode):
    Weight = sqrt(((Node.Position[0] - NextNode.Position[0])**2) + ((Node.Position[1] - NextNode.Position[1])**2))
    Node.Connections[NextNode] = Weight
    NextNode.Connections[Node] = Weight
    return Node


#Creating some nodes for testing
Node1 = Node(Name="Node 1", Position=(0,0))
Node2 = Node(Name="Node 2", Position=(0,5))
Node3 = Node(Name="Node 3", Position=(5,5))
Node4 = Node(Name="Node 4", Position=(3,10))
#Linking the nodes
NextTo(Node1, Node2)
NextTo(Node1, Node3)
NextTo(Node2, Node4)
NextTo(Node3, Node4)

#Original pathfinding algorithm that chooses the cheapest route
def PathFinding(Start,End):
    CurrentNode = Start
    ListOfNodesVisited = [Start]

    while CurrentNode != End:
        for i in ListOfNodesVisited:
            print(i.Name)
        for i in list(CurrentNode.Connections.keys()):
            if i in ListOfNodesVisited:
                CurrentNode.Connections.pop(i)
        NearestNode = {i:j for j, i in CurrentNode.Connections.items()}[min(CurrentNode.Connections.values())]
        CurrentNode = NearestNode
        ListOfNodesVisited.append(CurrentNode)

PathFinding(Node1, Node4)
print("Finished")

def AStar(Start,End):
    CurrentNode = Start
    CameFrom = {}
    CostSoFar = {}
    CameFrom[Start] = 0
    CostSoFar[Start] = 0

    while CurrentNode != End:

        CurrentNode.Connections

