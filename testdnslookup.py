import unittest
from dnslookup import gettype

class Testdnslookup(unittest.TestCase):
    def test_gettype_a(self):
        """testing A record check"""
        self.assertEqual(gettype(str(1)), "A")

    def test_gettype_ns(self):
        """testing NS record check"""
        self.assertEqual(gettype(str(2)), "NS")

    def test_gettype_cname(self):
        self.assertEqual(gettype(str(5)), "CNAME")
    
    def test_gettype_aaaa(self):
        self.assertEqual(gettype(str(28)), "AAAA")

if __name__ == "__main__":
    unittest.main()