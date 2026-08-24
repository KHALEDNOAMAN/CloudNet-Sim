import networkx as nx

class NetworkSimulator:
    def __init__(self):
        self.graph = nx.Graph()
        
    def add_node(self, name, ntype, ip, subnet):
        self.graph.add_node(name, type=ntype, ip=ip, subnet=subnet)
        
    def add_link(self, node1, node2, bandwidth, latency):
        self.graph.add_edge(node1, node2, bandwidth=bandwidth, latency=latency)
        
    def remove_node(self, name):
        self.graph.remove_node(name)
        
    def remove_link(self, node1, node2):
        self.graph.remove_edge(node1, node2)
        
    def ping(self, src, dst):
        try:
            path = nx.shortest_path(self.graph, src, dst)
            return {"success": True, "hops": len(path) - 1, "path": path}
        except nx.NetworkXNoPath:
            return {"success": False, "error": "No path found"}
            
    def traceroute(self, src, dst):
        return self.ping(src, dst)
        
    def get_routing_table(self, node):
        return {}
        
    def simulate_traffic(self, src, dst, protocol, size):
        return {"src": src, "dst": dst, "protocol": protocol, "size": size, "status": "delivered"}
