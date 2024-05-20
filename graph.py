# graph data structure includes nodes / vertices and edges that links one vertex to another 
# includes implementation of depth-first search and breadth-first search 
# note that DFS anf BFS has same pseudocode, it just depends on what DS
# is being used !!!

class Graph:
  def __init__(self):
    self.adjacency_list = {} # a dictionary to store the graph

  def add_vertex(self, vertex):
    if vertex not in self.adjacency_list:
        self.adjacency_list[vertex] = []

  def add_edge(self, vertex1, vertex2):
    if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list: # both valid vertices 
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
    else:
        raise ValueError("One or both vertices not found in graph")

  
  def dfs(self, start_vertex):
    visited = set()
    result = []

    def _dfs_recursive(vertex):
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                _dfs_recursive(neighbor)

    _dfs_recursive(start_vertex)
    return result

  def bfs(self, start_vertex):
    visited = set()
    queue = [start_vertex]
    result = []

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

if __name__ == "__main__":
  graph = Graph()
  graph.add_vertex("A")
  graph.add_vertex("B")
  graph.add_vertex("C")
  graph.add_vertex("D")
  graph.add_vertex("E")

  graph.add_edge("A", "B")
  graph.add_edge("A", "C")
  graph.add_edge("B", "D")
  graph.add_edge("C", "E")
  graph.add_edge("D", "E")

  print("DFS:", graph.dfs("A"))  # Output: DFS: ['A', 'B', 'D', 'E', 'C']
  print("BFS:", graph.bfs("A"))  # Output: BFS: ['A', 'B', 'C', 'D', 'E']
