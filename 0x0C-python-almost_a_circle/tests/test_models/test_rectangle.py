import unittest

from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    A test suite for the Rectangle class.
    """

    def test_rectangle_attributes(self):
        """
        Tests the default attributes of Rectangle.
        """
        r = Rectangle(3, 2)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_rectangle_attributes(self):
        """
        Tests custom attributes of Rectangle.
        """
        r = Rectangle(2, 3, 4, 5)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_area(self):
        """
        Tests the area method of Rectangle.
        """
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    def test_rectangle_update_attributes(self):
        """
        Tests the update method of Rectangle.
        """
        r = Rectangle(3, 2, 0, 0, 12)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_rectangle_to_dictionary(self):
        """
        Tests the to_dictionary method of Rectangle.
        """
        r = Rectangle(1, 2, 3, 4, 5)
        expected = {"x": 3, "y": 4, "id": 5, "height": 2, "width": 1}
        self.assertDictEqual(r.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
