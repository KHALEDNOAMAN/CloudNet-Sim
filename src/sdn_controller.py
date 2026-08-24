class SDNController:
    def __init__(self):
        self.flow_tables = {}
        
    def create_flow_rule(self, switch, match, action):
        if switch not in self.flow_tables:
            self.flow_tables[switch] = []
        rule = {"id": len(self.flow_tables[switch]), "match": match, "action": action}
        self.flow_tables[switch].append(rule)
        return rule["id"]
        
    def delete_flow_rule(self, switch, rule_id):
        if switch in self.flow_tables:
            self.flow_tables[switch] = [r for r in self.flow_tables[switch] if r["id"] != rule_id]
            
    def get_flow_table(self, switch):
        return self.flow_tables.get(switch, [])
        
    def load_balance(self, servers, algorithm="round-robin"):
        return servers[0] if servers else None
        
    def qos_policy(self, link, max_bandwidth, priority):
        pass
