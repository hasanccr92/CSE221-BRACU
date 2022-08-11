from queue import PriorityQueue
import math

##hasan's code
file1 = open('Task1In.txt',mode = 'r')
file2 = open("Task1Out.txt", mode = "w")

graph = {}
path = []

def Dijkstra(source, dest):
    
    dist = [math.inf] * 10
    dist[source] = 0
    visited = [0] * 10
    prev = {}
    pq = PriorityQueue()
    pq.put((dist[source],source))

    while pq.empty() != True:
        u = pq.get()[source] 
        if u not in visited:
            visited[u] = 1
            eg = graph[u]
            if eg != None:
                for i in eg:
                    v = i[0]
                    alt = dist[u]+i[1]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u
                        pq.put((dist[v],v))
        
    tmp = dest
    while tmp != source:
        path.append(tmp)
        tmp = prev[tmp]
    path.append(tmp)

    path.reverse()
    
    return dist[dest]




for i in range(int(file1.readline())):
    N, M = map(int, file1.readline().split())
    adj = [[] for x in range(N+1)]
    for j in range(M):
        u, v, w = map(int, file1.readline().split())
        adj[u].append((v, w))
    for i in range(N):
        graph[i] = adj[i]
    graph[N] = None
    print(graph)
    minDistance = Dijkstra(1, N)
    print("The minimum distance is : ", minDistance)
    print("The Path is :" , path)
    graph.clear()
    path.clear()



file1.close()
file2.close()