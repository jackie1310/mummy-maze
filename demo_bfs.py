from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
        
    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.graph:
            self.graph[vertex1].append(vertex2)
        else:
            self.graph[vertex1] = [vertex2]

        if vertex2 in self.graph:
            self.graph[vertex2].append(vertex1)
        else:
            self.graph[vertex2] = [vertex1]
            
    def bfs(self, node):
        visited = set()
        queue = deque([node])

        while queue:

            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
            
                for nei in self.graph[vertex]:
                    if nei not in visited:
                        queue.append(nei)
                        
    def addRectangleEdges(self):
        for row in range(self.numRows):
            for col in range(self.numCols):
                current = row * self.numCols + col
                # Kiểm tra và thêm cạnh tới đỉnh ở bên phải
                if col < self.numCols - 1:
                    self.addEdge(current, current + 1)
                # Kiểm tra và thêm cạnh tới đỉnh ở bên dưới
                if row < self.numRows - 1:
                    self.addEdge(current, current + self.numCols)

    def findAllShortestPaths(self, start, end):
        if start < 0 :
            return False

        queue = deque([[start]])
        shortest_paths = []
        visited = set([start])
        min_length = None

        while queue:
            path = queue.popleft()
            current = path[-1]

            for neighbor in self.adjList[current]:
                if neighbor in visited and (min_length is not None and len(path) >= min_length):
                    continue
                
                new_path = list(path)
                new_path.append(neighbor)

                if neighbor == end:
                    shortest_paths.append(new_path)
                    # shortest_paths.append(new_path[1]) # for game

                    min_length = len(new_path)
                else:
                    queue.append(new_path)
                    visited.add(neighbor)

        
        
        return shortest_paths


graph = Graph()
graph.addEdge(0,1)
graph.addEdge(0,2)
graph.addEdge(0,8)
graph.addEdge(2,3)
graph.addEdge(2,4)
graph.addEdge(2,6)
graph.addEdge(6,7)
graph.addEdge(6,5)
graph.addEdge(7,8)

graph.bfs(0)