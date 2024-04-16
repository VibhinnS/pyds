import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import unittest
from pyds.singlylinkedlist import SinglyLL

class TestSinglyLL(unittest.TestCase):
    def test_init(self):
        singly_ll = SinglyLL()
        self.assertIsNone(singly_ll.head)

    def test_add(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        self.assertEqual(singly_ll.head.data, 1)
        self.assertIsNone(singly_ll.head.next)

    def test_add_multiple(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.add(2)
        singly_ll.add(3)
        self.assertEqual(singly_ll.head.data, 1)
        self.assertEqual(singly_ll.head.next.data, 2)
        self.assertEqual(singly_ll.head.next.next.data, 3)
        self.assertIsNone(singly_ll.head.next.next.next)

    def test_addFirst(self):
        singly_ll = SinglyLL()
        singly_ll.add(2)
        singly_ll.addFirst(1)
        self.assertEqual(singly_ll.head.data, 1)
        self.assertEqual(singly_ll.head.next.data, 2)
        self.assertIsNone(singly_ll.head.next.next)

    def test_clear(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.clear()
        self.assertIsNone(singly_ll.head)

    def test_copy(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.add(2)
        copied_ll = singly_ll.copy()
        self.assertEqual(list(singly_ll), list(copied_ll))

    def test_get_head(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        self.assertEqual(singly_ll.get_head(), 1)

    def test_get_head_empty(self):
        singly_ll = SinglyLL()
        with self.assertRaises(Exception):
            singly_ll.get_head()

    def test_str(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.add(2)
        self.assertEqual(str(singly_ll), "1->2")

    def test_len(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.add(2)
        self.assertEqual(len(singly_ll), 2)

    def test_iter(self):
        singly_ll = SinglyLL()
        singly_ll.add(1)
        singly_ll.add(2)
        self.assertEqual(list(singly_ll), [1, 2])

    def test_addAtPosition(self):
        # Test adding at position 0
        singly_ll = SinglyLL()
        singly_ll.addAtPosition(1, 0)
        self.assertEqual(list(singly_ll), [1])

        # Test adding at position greater than 0
        singly_ll.addAtPosition(2, 1)
        singly_ll.addAtPosition(3, 2)
        self.assertEqual(list(singly_ll), [1, 2, 3])

    def test_addAtPosition_invalid_position(self):
        # Test adding at negative position
        singly_ll = SinglyLL()
        with self.assertRaises(ValueError):
            singly_ll.addAtPosition(1, -1)

    def test_addAtPosition_out_of_range(self):
        # Test adding at position out of range
        singly_ll = SinglyLL()
        singly_ll.add(1)
        with self.assertRaises(IndexError):
            singly_ll.addAtPosition(2, 2)


if __name__ == "__main__":
    unittest.main()
