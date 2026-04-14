# Dijkstra Algorithm Implementation
import heapq


class Graph:
    def __init__(self):
        self.adjacency_list = dict()

    def add_node(self, v):
        if v in self.adjacency_list:
            print(v,"is already present in graph")
        else:
            self.adjacency_list[v] = dict()
    
    def add_edge(self, v1, v2, weight):
        if v1 not in self.adjacency_list:
            print(v1, "is not present in graph")
        elif v2 not in self.adjacency_list:
            print(v2, "is not present in graph")
        else:
            self.adjacency_list[v1][v2] = weight
            self.adjacency_list[v2][v1] = weight

    # Rush Hour Scenario Weight change
    def modify_edge(self, v1, v2, weight):
        pass

    def dijkstra(self, start):
        # Distance & Previous Dictionary

        # Adds value float("inf") to keys in distance adjacency list
        distance = {item: float("inf") for item in self.adjacency_list}
        # The starting node value is set to 0
        distance[start] = 0
        # Creates Previous adjacency list
        previous = {node: None for node in self.adjacency_list}
        # Creating Priority Queue
        '''
        Use heapq.heappush() to add elements to queue
        Use heapq.heappop() to remove and return the smallest element
        '''
        queue = [(0,start)] # Tuple contains node and distance

        # While Queue is not empty
        while queue:
            # Returns the minimum distance
            current_distance, current_node = heapq.heappop(queue)

            # For loop node and weight from adjacency
            for node, weight in self.adjacency_list[current_node].items():
                new_distance = current_distance + weight

                if new_distance < distance[node]:
                    distance[node] = new_distance
                    previous[node] = current_node
                    heapq.heappush(queue, (new_distance, node))
        return distance, previous

    def findShortestPath(self, start, target):
        distance, previous = self.dijkstra(start)
        path = []
        current_node = target
        while current_node:
            path.append(current_node)
            current_node = previous[current_node]
        return f"The shortest path from {start} to {target} is : {path[::-1]} and takes {distance[target]} minutes"
