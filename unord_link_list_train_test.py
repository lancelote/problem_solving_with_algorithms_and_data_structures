import unittest
from unord_link_list_train import Node, LinkedList


class NodeTest(unittest.TestCase):

    def setUp(self):
        self.test_node = Node()

    def test_get_item(self):
        self.assertEqual(self.test_node.get_item(), None)

    def test_set_item(self):
        self.test_node.set_item(0)
        self.assertEqual(self.test_node.get_item(), 0)

    def test_get_next(self):
        self.assertEqual(self.test_node.get_next(), None)

    def test_set_next(self):
        next_node = Node(0)
        self.test_node.set_next(next_node)
        self.assertEqual(self.test_node.get_next(), next_node)


class LinkedListTest(unittest.TestCase):

    # ToDo : complete
    pass

if __name__ == '__main__':
    unittest.main()