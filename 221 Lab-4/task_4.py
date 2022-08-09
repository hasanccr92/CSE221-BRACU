# -*- coding: utf-8 -*-
"""task-4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1otnQg8J0BGgX6bC1SpzdJrFF2xyWjyUr
"""

#---------Task-4---------#
file1 = open('task4In.txt','r')
file2 = open('task4Out.txt','w')

from queue import PriorityQueue
import math

def Dijkstra(source, dest):
    
    dist[source] = 0
    prev = {}
    pq = PriorityQueue()
    pq.put((dist[source],source))

    while pq.empty() != True:
        u = pq.get()[1]
        if visited[u]:
            continue
        visited[u] = True
        if u in graph:
            for vertex in graph[u]:
                if dist[vertex[0]] > dist[u] + vertex[1]:
                    dist[vertex[0]] = dist[u] + vertex[1]
                    prev[vertex[0]] = u
                    pq.put((dist[vertex[0]],vertex[0]))

    tmp = dest
    while tmp != source:
        path.append(tmp)
        tmp = prev[tmp]
    path.append(tmp)

    # print(prev)
    path.reverse()
    file2.write('The shortest distance is '+str(dist[dest]))

visited = {}
dist = {}
graph = dict()
path = []
for i in range(18):
    u,v,w = file1.readline().split()
    graph.setdefault(u,[])
    graph[u].append([v,int(w)])
    dist[u] = math.inf
    dist[v] = math.inf
    visited[u] = False
    visited[v] = False

# print(graph)
Dijkstra("Motijheel",'MOGHBAZAR')
file2.write("\nThe Path is :" + str(path))