import unittest
from src.firewall import Firewall

class TestFirewall(unittest.TestCase):
    def test_default_policy(self):
        fw = Firewall()
        self.assertEqual(fw.default_action, "DENY")
