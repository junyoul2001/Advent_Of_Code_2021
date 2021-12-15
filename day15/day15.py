import heapq

def dijkstra(graph, start_point):
    start_x, start_y = start_point

    distances = [[float('inf') for y in range(len(graph[0]))] for x in range(len(graph))]
    distances[start_x][start_y] = 0

    pq = [start_point]
    while len(pq) > 0:
        coord = heapq.heappop(pq)
        x, y = coord[0], coord[1]

        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            new_x = x+i if x+i >= 0 and x+i < len(graph) else x
            new_y = y+j if y+j >= 0 and y+j < len(graph[0]) else y

            new_distance = distances[x][y] + graph[new_x][new_y]
            if new_distance < distances[new_x][new_y]:
                distances[new_x][new_y] = new_distance
                heapq.heappush(pq,(new_x, new_y))

    return distances[-1][-1]

def prob1(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(list(line.strip()))
    graph = [[int(y) for y in x] for x in input_array]

    return dijkstra(graph,(0,0))

def prob2(file):
    input = open(file, "r").readlines()
    input_array = []

    for line in input:
        input_array.append(list(line.strip()))
    graph = [[int(y) for y in x] for x in input_array]
    new_graph = [[0 for y in range(len(graph[0]) * 5)] for x in range(len(graph) * 5)]

    for x in range(len(new_graph)):
        for y in range(len(new_graph[0])):
            init_x = x // len(graph)
            init_y = y // len(graph[0])

            new_value = graph[x % len(graph)][y % len(graph[0])] + init_x + init_y
            new_value = new_value - 9 if new_value > 9 else new_value

            new_graph[x][y] = new_value
            
    return dijkstra(new_graph, (0,0))