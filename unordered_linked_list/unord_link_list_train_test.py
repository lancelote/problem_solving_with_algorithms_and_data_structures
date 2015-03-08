import unittest
from unordered_linked_list.unord_link_list_train import Node, LinkedList

# ToDo : add tests for inadequate input


class NodeTest(unittest.TestCase):

    def setUp(self):
        self.test_node = Node()

    def test_get_item(self):
        self.assertIsNone(self.test_node.get_item())

    def test_set_item(self):
        self.test_node.set_item(0)
        self.assertEqual(self.test_node.get_item(), 0)

    def test_get_next(self):
        self.assertIsNone(self.test_node.get_next())

    def test_set_next(self):
        next_node = Node(0)
        self.test_node.set_next(next_node)
        self.assertEqual(self.test_node.get_next(), next_node)


class LinkedListTest(unittest.TestCase):

    def setUp(self):
        self.test_list = LinkedList()

    def test_eq_returns_correct_result(self):
        lst1 = LinkedList()
        lst1.add(1)
        lst1.add(2)
        lst2 = LinkedList()
        lst2.add(1)
        lst2.add(2)
        self.assertTrue(lst1 == lst2)
        lst2.add(3)
        self.assertFalse(lst1 == lst2)

    def test_is_empty(self):
        self.assertTrue(self.test_list.is_empty())

    def test_add(self):
        self.test_list.add(1)
        self.test_list.add(2)
        self.assertEqual(self.test_list.head.get_item(), 2)

    def test_print_lst(self):
        self.test_list.add(1)
        self.test_list.add(2)
        self.assertEqual(self.test_list.print_lst(), "[2] [1]")

    def test_reverse(self):
        self.test_list.add(1)
        self.test_list.add(2)
        self.test_list.reverse()
        self.assertEqual(self.test_list.head.get_item(), 1)

    def test_size(self):
        self.assertEqual(self.test_list.size(), 0)
        self.test_list.add(0)
        self.assertEqual(self.test_list.size(), 1)
        self.test_list.add(1)
        self.assertEqual(self.test_list.size(), 2)

    def test_search(self):
        self.test_list.add(1)
        self.assertFalse(self.test_list.search(0))
        self.assertTrue(self.test_list.search(1))

    def test_remove(self):
        self.assertFalse(self.test_list.remove(1))
        self.test_list.add(1)
        self.test_list.add(2)
        self.assertTrue(self.test_list.remove(2))
        self.assertEqual(self.test_list.head.get_item(), 1)
        self.test_list.remove(1)
        self.assertIsNone(self.test_list.head)
        self.test_list.add(1)
        self.test_list.add(2)
        self.test_list.add(3)
        self.assertTrue(self.test_list.remove(1))
        self.assertEqual(self.test_list.print_lst(), "[3] [2]")

    def test_append(self):
        self.test_list.add(1)
        self.test_list.append(0)
        self.test_list.append(-1)
        self.assertEqual(self.test_list.head.get_item(), 1)

    def test_index(self):
        self.assertFalse(self.test_list.index(1))
        self.test_list.add(0)
        self.test_list.add(1)
        self.test_list.add(2)
        self.assertEqual(self.test_list.index(0), 2)
        self.assertEqual(self.test_list.index(1), 1)
        self.assertEqual(self.test_list.index(2), 0)

    def test_insert(self):
        self.test_list.insert(0, 0)
        self.assertEqual(self.test_list.head.get_item(), 0)
        self.test_list.insert(1, 0)
        self.assertEqual(self.test_list.print_lst(), "[1] [0]")
        self.test_list.insert(2, 1)
        self.assertEqual(self.test_list.print_lst(), "[1] [2] [0]")

    def test_pop(self):
        self.test_list.add(0)
        self.test_list.add(1)
        self.test_list.add(2)
        self.test_list.pop(1)
        self.assertEqual(self.test_list.print_lst(), "[2] [0]")
        self.test_list.pop(0)
        self.assertEqual(self.test_list.print_lst(), "[0]")
        self.test_list.pop(0)
        self.assertIsNone(self.test_list.head)

if __name__ == '__main__':
    unittest.main()