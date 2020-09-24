import sys
from collections import deque 
import math, time
sys.stdin = open("input.txt", 'r')

from graph import Graph

class Node:
    def __init__(self, name:str, parent:str):
        self.name = name
        self.parent = parent
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost

class Min_distance:
    def __init__(self, graph : Graph, start, end):
        self.graph = graph
        self.start = start
        self.end = end
        self.visited = {}
        self.path = deque()
        self.path_taken = deque()
        self.min_dist = math.inf
    
    def reset(self):
        visited = {}
        for i in self.graph.all_nodes():
            visited[i] = False
        self.visited = visited
        self.path.clear()
        self.path_taken.clear()
        self.min_dist = math.inf
    
    def dfs_cover(self, cur, dist):
        self.visited[cur] = True
        self.path.append((cur,dist))
        if(cur == self.end):
            if(dist < self.min_dist):
                self.min_dist = dist
                self.path_taken = self.path.copy()
        else:
            neighbour = self.graph.get(cur)
            for (i,dist_i) in neighbour.items():
                if(self.visited[i]):
                    continue
                self.dfs_cover(i, dist+dist_i)
        self.path.pop()
        self.visited[cur] = False

    def dfs(self):
        self.reset()
        self.dfs_cover(self.start, 0)
        print(self.path_taken)
    
    def isVisited(self, a, path):
        for (i,j) in path:
            if(a == i):
                return True
        return False

    def bfs(self):
        self.reset()
        path = deque()
        path.append((self.start,0))
        queue = deque()
        queue.append(path)
        while(len(queue) != 0):
            path = queue.popleft()
            last_node, dist_till = path[-1]
            if(last_node == self.end):
                if(dist_till < self.min_dist):
                    self.min_dist = dist_till
                    self.path_taken = path.copy()
            else:
                neighbour = self.graph.get(last_node)
                for (b, dist) in neighbour.items():
                    if(self.isVisited(b, path)):
                        continue
                    new_path = path.copy()
                    new_path.append((b, dist_till+dist))
                    queue.append(new_path)
        print(self.path_taken)

    def dist_huristics(self, heuristics, g, h):
        self.reset()
        open = []
        closed = []
        start_node = Node(self.start, None)
        goal_node = Node(self.end, None)
        open.append(start_node)
        while len(open) > 0:
            open.sort(key= lambda z: z.g*g + z.h*h)
            current_node = open.pop(0)
            closed.append(current_node)
            if current_node.name == goal_node.name:
                path = []
                while current_node.name != start_node.name:
                    path.append((current_node.name,current_node.g))
                    current_node = current_node.parent
                path.append((start_node.name, start_node.g))
                return path[::-1]
            neighbors = self.graph.get(current_node.name)
            for key, value in neighbors.items():
                neighbor = Node(key, current_node)
                if(neighbor in closed):
                    continue
                neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
                neighbor.h = heuristics.get(neighbor.name)
                neighbor.f = neighbor.h
                if(self.add_to_open(open, neighbor, g, h) == True):
                    open.append(neighbor)

    def add_to_open(self, open, neighbor, g = 1, h = 1):
        for node in open:
            if (neighbor.name == node.name and ((neighbor.g*g + neighbor.h*h) >= (node.g*g + node.h*h))):
                return False
        return True
    
    def a_star(self, heuristics):
        print(self.dist_huristics(heuristics, 1, 1))
    
    def best_first_search(self, heuristics):
        print(self.dist_huristics(heuristics, 0, 1))
    

graph = Graph()
graph.make_undirected()
for i in range(int(input().rstrip())):
    a,b,dist = input().rstrip().split()
    graph.connect(a, b, int(dist))

heuristics = {}
for i in range(int(input().rstrip())):
    a,b =  input().rstrip().split()
    heuristics[a] = int(b)

distance = Min_distance(graph, 'Frankfurt', 'Ulm')


time_start = time.time()
distance.dfs()
print("time taken by DFS", time.time() - time_start)
time_start = time.time()
distance.bfs()
print("time taken by BFS", time.time() - time_start)
time_start = time.time()
distance.a_star(heuristics)
print("time taken by a_star", time.time() - time_start)
time_start = time.time()
distance.best_first_search(heuristics)
print("time taken by best_first_search", time.time() - time_start)


