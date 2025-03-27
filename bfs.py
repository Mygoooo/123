import csv
from collections import deque
edgeFile = 'edges.csv'

def read_graph():
    """
    Read the edges from the CSV file and build an adjacency list representation of the graph.
    """
    graph = {}
    
    with open(edgeFile, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # This skips the first line (header)
        for row in reader:
            node1, node2, dist = int(row[0]), int(row[1]), float(row[2])
            
            # Add the edge from node1 to node2 (directed graph)
            if node1 not in graph:
                graph[node1] = []
            
            # Add the edge with the distance from node1 -> node2
            graph[node1].append((node2, dist))
    
    return graph

def bfs(start, end):
    # Begin your code (Part 1)
    # Load the graph
    graph = read_graph()
    
    # BFS initialization
    queue = deque([(start, [start], 0)])  # (current_node, path_so_far, accumulated_distance)
    visited = set()  # To track visited nodes
    num_visited = 0  # To count number of nodes visited
    
    while queue:
        current_node, path, accumulated_distance = queue.popleft()
        visited.add(current_node)
        num_visited += 1

        
        # If we reached the end node, return the path, distance, and number of visited nodes
        if current_node == end:
            return path, accumulated_distance, num_visited
        
        # Explore neighbors
        for neighbor, edge_cost in graph.get(current_node, []):  # Use get() to avoid KeyError when no neighbors
            if neighbor not in visited:
                new_path = path + [neighbor]
                new_distance = accumulated_distance + edge_cost
                queue.append((neighbor, new_path, new_distance))
    
    # If there's no path to the end node
    return [], 0, num_visited
    # End your code (Part 1)


if __name__ == '__main__':
    path, dist, num_visited = bfs(2270143902, 1079387396)
    print(f'The number of path nodes: {len(path)}')
    print(f'Total distance of path: {dist}')
    print(f'The number of visited nodes: {num_visited}')
