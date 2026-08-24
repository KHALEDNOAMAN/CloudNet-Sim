class TrafficShaper:
    def __init__(self):
        self.links = {}
        
    def set_bandwidth_limit(self, link, max_mbps):
        self.links[link] = {"bandwidth": max_mbps}
        
    def set_latency(self, link, ms):
        if link not in self.links: self.links[link] = {}
        self.links[link]["latency"] = ms
        
    def set_packet_loss(self, link, percent):
        if link not in self.links: self.links[link] = {}
        self.links[link]["loss"] = percent
        
    def simulate_congestion(self, link):
        pass
        
    def get_link_stats(self, link):
        return self.links.get(link, {})
