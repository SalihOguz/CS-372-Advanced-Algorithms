from Queue import PriorityQueue

def find_shortest_path(G):
    # creating graph
    graph = {}
    for x in range(len(G)):
        for y in range(len(G[0])):
            if G[x][y] == "X":
                continue
            graph.setdefault((x,y), {})
            if y > 0:  # left
                if G[x][y-1] == "X":
                    if y > 1:
                        if G[x][y-2] != "X":
                            graph[(x, y)][x, y - 2] = G[x][y-2] * 2
                else:
                    graph[(x, y)][x, y - 1] = G[x][y - 1]

            if y < len(G[0]) - 1:  # right
                if G[x][y+1] == "X":
                    if y < len(G[0])-2:
                        if G[x][y+2] != "X":
                            graph[(x, y)][x, y + 2] = G[x][y+2] * 2
                else:
                    graph[(x, y)][x, y + 1] = G[x][y + 1]

            if x > 0:  # up
                if G[x - 1][y] == "X":
                    if x > 1:
                        if G[x - 2][y] != "X":
                            graph[(x, y)][x-2, y] = G[x-2][y] * 2
                else:
                    graph[(x, y)][x-1, y] = G[x - 1][y]

            if x < len(G) - 1:  # down
                if G[x + 1][y] == "X":
                    if x < len(G)-2:
                        if G[x + 2][y] != "X":
                            graph[(x, y)][x+2, y] = G[x+2][y] * 2
                else:
                    graph[(x, y)][x+1, y] = G[x + 1][y]

    path = []
    visited = []
    visitedNodes = []

    queue = PriorityQueue()
    queue.put((0, (0, 0), ()))
    final = []

    while queue:
        cost, point, parent = queue.get()
        if point not in visited:
            visited.append(point)
            visitedNodes.append((point, parent))
            if point == (len(G)-1, len(G[0])-1):
                final = (point, parent)
                break
            for neighbor in graph[point]:
                if neighbor not in visited:
                    queue.put((graph[point][neighbor], neighbor, point))
    path.append(final[0])
    minCost = 0
    for i in visitedNodes[::-1]:
        if i[0] == final[1]:
            minCost += graph[i[0]][final[0]]
            path.append(i[0])
            final = i

    print "Steps:", len(path), "\nMinimum Cost:", minCost, "\nPath:", path[::-1]
    return path[::-1]

def find_shortest_path_with_negative_costs(G):
    # creating graph
    graph = {}
    for x in range(len(G)):
        for y in range(len(G[0])):
            if G[x][y] == "X":
                continue
            graph.setdefault((x, y), {})
            if y > 0:  # left
                if G[x][y - 1] == "X":
                    if y > 1:
                        if G[x][y - 2] != "X":
                            graph[(x, y)][x, y - 2] = G[x][y - 2] * 2
                else:
                    graph[(x, y)][x, y - 1] = G[x][y - 1]

            if y < len(G[0]) - 1:  # right
                if G[x][y + 1] == "X":
                    if y < len(G[0]) - 2:
                        if G[x][y + 2] != "X":
                            graph[(x, y)][x, y + 2] = G[x][y + 2] * 2
                else:
                    graph[(x, y)][x, y + 1] = G[x][y + 1]

            if x > 0:  # up
                if G[x - 1][y] == "X":
                    if x > 1:
                        if G[x - 2][y] != "X":
                            graph[(x, y)][x - 2, y] = G[x - 2][y] * 2
                else:
                    graph[(x, y)][x - 1, y] = G[x - 1][y]

            if x < len(G) - 1:  # down
                if G[x + 1][y] == "X":
                    if x < len(G) - 2:
                        if G[x + 2][y] != "X":
                            graph[(x, y)][x + 2, y] = G[x + 2][y] * 2
                else:
                    graph[(x, y)][x + 1, y] = G[x + 1][y]

    path = []
    visited = []
    visitedNodes = []

    queue = PriorityQueue()
    queue.put((0, (0, 0), ()))
    final = []

    while queue:
        cost, point, parent = queue.get()
        if point not in visited:
            visited.append(point)
            visitedNodes.append((point, parent))
            if point == (len(G) - 1, len(G[0]) - 1):
                final = (point, parent)
                break
            for neighbor in graph[point]:
                if neighbor not in visited:
                    queue.put((graph[point][neighbor], neighbor, point))
    path.append(final[0])
    minCost = 0
    for i in visitedNodes[::-1]:
        if i[0] == final[1]:
            minCost += graph[i[0]][final[0]]
            path.append(i[0])
            final = i

    print "Steps:", len(path), "\nMinimum Cost:", minCost, "\nPath:", path[::-1]

def find_shortest_path_with_checkpoint(G):
    pass

G = [[0, "X", 1, 4, 9, "X"], [7, 7, 4, "X", 4, 8], [3, "X", 3, 2, "X", 4], [10, 2, 5, "X", 3, 0]]
G2 = [[0, "X", 5, -3, 6, "X"], [6, -4, 5, "X", 3, -8], [4, "X", 3, -7, "X", 5], [10, 2, -2, "X", 6, 0]]
G3 = [[0, 6, "Check", 4, 9, 3], [5, 7, 4, 6, "Check", 3], [3, "Check", 6, 5, 8, 4], [10, 2, 5, 4, 3, 0]]
#find_shortest_path(G2)
find_shortest_path_with_checkpoint(G3)