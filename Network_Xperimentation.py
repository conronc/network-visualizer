# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 13:16:19 2020

@author: croncaioli
"""

import networkx as nx
from random import randint, sample
import matplotlib.pyplot as plt

#Feed in values

numNodes = 25 #population of random graph

initInfected = 1  #num initial infected

#

G = nx.random_powerlaw_tree(numNodes,gamma=2.5, tries = 10000)

for i in G.nodes():
    G.nodes[i]['bool'] = False

for i in sample(G.nodes(),initInfected):
    G.nodes[i]['bool'] = True




#node walking algorithm for network
def randFriendIter(network):
    iterNodes = []
    for i in network:
        if network.nodes[i]['bool']:
            iterNodes.append(sample(list(G[i]),1)[0])
            network.nodes[i]['bool'] = False
    for j in iterNodes:
        network.nodes[j]['bool'] = True
    return 0

#temporary coloring solutions
#applies a color associated with true/false boolian value in network
def colorNetwork(network):
    nodeColorArray=[]
    for i in network:
        if network.nodes[i]['bool']:
            nodeColorArray.append('red')
        else:
            nodeColorArray.append('blue')
    return nodeColorArray

   
    
#This doesn't actually work, higher level 'infections' can get overwritten
#for j in G:
#    if G.nodes[j]['bool']:
#        for k in G[j]:
#            for l in G[k]:
#                for m in G[l]:
#                    nodeColorArray[m] = 'green'
#                nodeColorArray[l] = 'yellow'
#            nodeColorArray[k] = 'orange'
#        nodeColorArray[j] = 'red'
                
#end coloring section
    
plt.subplot(121)
    
nx.draw_kamada_kawai(G, node_color = colorNetwork(G))

plt.subplot(122)

randFriendIter(G)

nx.draw_kamada_kawai(G, node_color = colorNetwork(G))


