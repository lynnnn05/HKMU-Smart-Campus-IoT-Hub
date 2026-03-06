import heapq

class NetworkManager:
    def __init__(self, region_name):
        self.region_name = region_name
        # Data Structure: Graph
        # Use Adjacency List to store network topology
        # Format: { 'Node_A': {'Node_B': latency1, 'Node_C': latency2}, ... }
        self.network_graph = {}
        
        # Combining OOP concepts from Task 1: Use a list to specifically manage sensor objects registered to the network
        self.registered_sensors = [] 

    def register_device(self, sensor_obj):
        """Register the sensor object created in Task 1 to the network"""
        if sensor_obj not in self.registered_sensors:
            self.registered_sensors.append(sensor_obj)
            print(f"Success: {sensor_obj.sensor_id} is now registered to {self.region_name} Network.")

    def add_node(self, node_id):
        """Add a network node to the graph (e.g., router, base station, or central server)"""
        if node_id not in self.network_graph:
            self.network_graph[node_id] = {}

    def add_connection(self, node1, node2, latency):
        """
        Add an undirected edge to the graph
        Represents the communication link between two nodes, where latency represents the weight
        """
        self.add_node(node1)
        self.add_node(node2)
        # Bidirectional connection
        self.network_graph[node1][node2] = latency
        self.network_graph[node2][node1] = latency

    def find_optimal_route(self, start_node, target_node):
        """
        Algorithm: Dijkstra's Shortest Path Algorithm
        Used to find the lowest latency route for data packets from start to target in complex embedded networks.
        """
        # Initialize distances of all nodes to infinity
        distances = {node: float('inf') for node in self.network_graph}
        distances[start_node] = 0
        
        # Record the path to easily print out specific route nodes at the end
        previous_nodes = {node: None for node in self.network_graph}
        
        # Priority Queue, storing (current_total_latency, node_name)
        pq = [(0, start_node)]

        while pq:
            # Pop the node with the minimum current latency
            current_distance, current_node = heapq.heappop(pq)

            # If the target node is found, terminate early
            if current_node == target_node:
                break

            # If the popped node's distance is greater than the recorded shortest distance, it's redundant data, skip
            if current_distance > distances[current_node]:
                continue

            # Iterate through all neighbors of the current node
            for neighbor, weight in self.network_graph[current_node].items():
                distance = current_distance + weight

                # If a shorter path is found, update the distance and push it into the priority queue
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Backtrack to construct the shortest path
        path = []
        curr = target_node
        while curr is not None:
            path.append(curr)
            curr = previous_nodes[curr]
        path.reverse() # Reverse the list since it was backtracked in reverse order

        # If start and target nodes are not connected
        if distances[target_node] == float('inf'):
            return None, float('inf')

        return path, distances[target_node]
