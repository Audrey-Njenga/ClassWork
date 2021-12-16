def spanningTree( V, adj):
    # track included nodes
    mst = [False for x in range(V)]
    # track included weights
    keys = [float('inf') for v in range(V)]
    keys[0] = 0
    path = [None]*V

    # helper function to find node with min weight
    def minVertex(keys, mst):
        minKey = float('inf')
        for y in range(len(keys)):
            if keys[y] < minKey and not mst[y]:
                minKey = keys[y]
                minIndex = y
        return minIndex

    path[0] = -1
    # while all nodes are not included in mst
    for v in range(V):
        minVal = minVertex(keys, mst)
        mst[minVal] = True
        for x in range(len(adj[minVal])):
            if adj[minVal][x] != 0 and mst[x] == False and adj[minVal][x] < keys[x]:
                keys[x] = adj[minVal][x]
                path[x] =minVal
    # return total weighted sum of minimum spanning tree
    for p in range(1,V):
        print(str(path[p]), str(p) + ": " +  str(adj[p][path[p]]))
    return sum(keys)



print(spanningTree(5, [[0, 2, 0, 6, 0],
                    [2, 0, 3, 8, 5],
                    [0, 3, 0, 0, 7],
                    [6, 8, 0, 0, 9],
                    [0, 5, 7, 9, 0]]))