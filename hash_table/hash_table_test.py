import unittest
from hash_table.hash_table import HashTable


class HashTableTest(unittest.TestCase):

    def setUp(self):
        self.test_hash_table = HashTable()

        self.test_hash_table.put(54, "cat")
        self.test_hash_table.put(26, "dog")
        self.test_hash_table.put(93, "lion")
        self.test_hash_table.put(17, "tiger")
        self.test_hash_table.put(77, "bird")
        self.test_hash_table.put(31, "cow")
        self.test_hash_table.put(44, "goat")
        self.test_hash_table.put(55, "pig")
        self.test_hash_table.put(20, "chicken")

    def test_init_works_correct(self):
        self.assertEqual(HashTable().size, 11)
        self.assertEqual(HashTable().slots, [None]*self.test_hash_table.size)
        self.assertEqual(HashTable().data, [None]*self.test_hash_table.size)

    def test_hash_returns_correct_result(self):
        self.assertEqual(HashTable.hash_function(54, self.test_hash_table.size), 10)
        self.assertEqual(HashTable.hash_function(26, self.test_hash_table.size), 4)
        self.assertEqual(HashTable.hash_function(93, self.test_hash_table.size), 5)
        self.assertEqual(HashTable.hash_function(17, self.test_hash_table.size), 6)
        self.assertEqual(HashTable.hash_function(77, self.test_hash_table.size), 0)
        self.assertEqual(HashTable.hash_function(31, self.test_hash_table.size), 9)
        self.assertEqual(HashTable.hash_function(44, self.test_hash_table.size), 0)
        self.assertEqual(HashTable.hash_function(55, self.test_hash_table.size), 0)
        self.assertEqual(HashTable.hash_function(20, self.test_hash_table.size), 9)

    def test_rehash_returns_correct_result(self):
        self.assertEqual(HashTable.rehash(0, self.test_hash_table.size), 1)
        self.assertEqual(HashTable.rehash(5, self.test_hash_table.size), 6)
        self.assertEqual(HashTable.rehash(10, self.test_hash_table.size), 0)

    def test_put_works_correct(self):
        self.assertEqual(self.test_hash_table.slots, [77, 44, 55, 20, 26, 93, 17, None, None, 31, 54])
        self.assertEqual(self.test_hash_table.data, ['bird', 'goat', 'pig', 'chicken', 'dog', 'lion', 'tiger', None,
                                                     None, 'cow', 'cat'])

    def test_get_works_correct(self):
        self.assertEqual(self.test_hash_table.get(54), "cat")
        self.assertEqual(self.test_hash_table.get(26), "dog")
        self.assertEqual(self.test_hash_table.get(93), "lion")
        self.assertEqual(self.test_hash_table.get(17), "tiger")
        self.assertEqual(self.test_hash_table.get(77), "bird")
        self.assertEqual(self.test_hash_table.get(31), "cow")
        self.assertEqual(self.test_hash_table.get(44), "goat")
        self.assertEqual(self.test_hash_table.get(55), "pig")
        self.assertEqual(self.test_hash_table.get(20), "chicken")
        self.assertIsNone(self.test_hash_table.get(18))

    def test_getitem_returns_correct_value(self):
        self.assertEqual(self.test_hash_table[54], "cat")

    def test_set_item_works_correct(self):
        self.test_hash_table[18] = "monkey"
        self.assertEqual(self.test_hash_table[18], "monkey")