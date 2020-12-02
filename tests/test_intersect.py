import unittest

from intersect.quadtrees import Path, check_intersection


class TestIntersect(unittest.TestCase):
    def test_intersect(self):
        p1 = Path((0, 0), (10, 10))
        p2 = Path((10, 0), (0, 10))
        print(p1, p2)
        self.assertTrue(check_intersection([p1, p2]))
