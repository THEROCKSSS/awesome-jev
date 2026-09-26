import unittest

from scripts.update_list import relevant


class DiscoveryTests(unittest.TestCase):
    def test_product_name_cannot_be_assembled_across_fields(self):
        unrelated = {"name": "design-system", "description": "One token architecture for UI", "owner": {"login": "other"}, "homepage": ""}
        self.assertFalse(relevant(unrelated))
        self.assertTrue(relevant({**unrelated, "description": "Uses TypeSafe Jev to route actions"}))


if __name__ == "__main__":
    unittest.main()
