class VLANManager:
    def __init__(self):
        self.vlans = {}
        self.ports = {}
        
    def create_vlan(self, vid, name, subnet):
        self.vlans[vid] = {"name": name, "subnet": subnet, "members": []}
        
    def assign_port(self, switch, port, vlan_id):
        self.ports[f"{switch}:{port}"] = vlan_id
        if vlan_id in self.vlans:
            self.vlans[vlan_id]["members"].append(f"{switch}:{port}")
            
    def inter_vlan_routing(self, router, vlan1, vlan2):
        pass
        
    def get_vlan_members(self, vlan_id):
        return self.vlans.get(vlan_id, {}).get("members", [])
        
    def calculate_subnet(self, cidr):
        return {"network": cidr, "broadcast": cidr, "usable": []}
