import unittest

from models.square import Square


class TestSquare(unittest.TestCase):
    """
    A test suite for the Square class.
    """

    def test_square_size(self):
        """
        Tests the size attribute of Square.
        """
        s = Square(4)
        self.assertEqual(s.size, 4)

    def test_square_custom_size(self):
        """
        Tests the custom size attribute of Square.
        """
        s = Square(6)
        self.assertEqual(s.size, 6)

    def test_square_area(self):
        """
        Tests the area method of Square.
        """
        s = Square(3)
        self.assertEqual(s.area(), 9)

    def test_square_str(self):
        """
        Tests the __str__ method of Square.
        """
        s = Square(3, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 3")

    def test_square_update(self):
        """
        Tests the update method of Square.
        """
        s = Square(2, 0, 0, 1)
        s.update(89, 3)
        self.assertEqual(s.id, 89)
        self.assertEqual(s.size, 3)

    def test_square_to_dictionary(self):
        """
        Tests the to_dictionary method of Square.
        """
        s = Square(1, 2, 3, 4)
        expected = {"id": 4, "x": 2, "size": 1, "y": 3}
        self.assertDictEqual(s.to_dictionary(), expected)


if __name__ == "__main__":
    unittest.main()
