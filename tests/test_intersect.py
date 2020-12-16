import unittest


class TestIntersect(unittest.TestCase):
    def test_poi(self):
        from line_intersect_2d.basics import Segment, Point

        s = Segment(Point(50.02185544718787, 21.993619530941572), Point(50.02176723839346, 21.991951204026883))
        s2 = Segment(Point(50.02173025388135, 21.992036926762236), Point(50.02182018594027, 21.992036930316072))
        s.intersection_point(s2)

    def test_intersect(self):
        from line_intersect_2d.quadtrees import Path, check_intersection

        p1 = Path((0, 0), (10, 10))
        p2 = Path((10, 0), (0, 10))
        self.assertTrue(check_intersection([p1, p2]))

    def test_not_intersect(self):
        from line_intersect_2d.quadtrees import Path, check_intersection

        p1 = Path((0, 0), (0, 10))
        p2 = Path((10, 0), (10, 10))
        self.assertIsNone(check_intersection([p1, p2]))
