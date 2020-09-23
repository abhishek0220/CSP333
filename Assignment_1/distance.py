import sys
from collections import deque 
import math, time
sys.stdin = open("input.txt", 'r')

from graph import Graph

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
        distace_from_start = {}
        for i in self.graph.all_nodes():
            distace_from_start[i] = math.inf

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
        


graph = Graph()
graph.make_undirected()
for i in range(int(input().rstrip())):
    a,b,dist = input().rstrip().split()
    graph.connect(a, b, int(dist))

distance = Min_distance(graph, 'Frankfurt', 'Ulm')
time_start = time.time()
distance.dfs()
print("time taken by DFS", time.time() - time_start)
time_start = time.time()
distance.bfs()
print("time taken by BFS", time.time() - time_start)


