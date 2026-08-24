class Firewall:
    def __init__(self):
        self.rules = []
        self.default_action = "DENY"
        self.blocked_logs = []
        
    def add_rule(self, action, protocol, src, dst, port):
        rule = {"id": len(self.rules), "action": action, "protocol": protocol, "src": src, "dst": dst, "port": port}
        self.rules.append(rule)
        return rule["id"]
        
    def delete_rule(self, rule_id):
        self.rules = [r for r in self.rules if r["id"] != rule_id]
        
    def evaluate_packet(self, packet):
        return self.default_action == "ALLOW"
        
    def get_rules(self):
        return self.rules
        
    def default_policy(self, action):
        self.default_action = action
        
    def log_blocked_packets(self):
        return self.blocked_logs
        
    def stateful_inspection(self):
        pass
