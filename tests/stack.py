import sys
import os
import unittest
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from pyds.stack.stack import AStack, LLStack, StackOverFlowError, StackUnderFlowError

class TestAStack(unittest.TestCase):
    def test_push_pop(self):
        stack = AStack(int, size=3)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_push_full_stack(self):
        stack = AStack(int, size=2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(StackOverFlowError):
            stack.push(3)

    def test_pop_empty_stack(self):
        stack = AStack(int)
        with self.assertRaises(StackUnderFlowError):
            stack.pop()


class TestLLStack(unittest.TestCase):
    def test_push_pop(self):
        stack = LLStack(int, size=3)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)

    def test_push_full_stack(self):
        stack = LLStack(int, size=2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(StackOverFlowError):
            stack.push(3)

    def test_pop_empty_stack(self):
        stack = LLStack(int)
        with self.assertRaises(StackUnderFlowError):
            stack.pop()


if __name__ == "__main__":
    unittest.main()
