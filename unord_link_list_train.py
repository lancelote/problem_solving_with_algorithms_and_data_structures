class Node:
    def __init__(self, init_data=None):
        self.item = init_data
        self.next = None

    def __eq__(self, other):
        return self.get_next() == other.get_next() and self.get_item() == other.get_item()

    def set_item(self, new_data):
        self.item = new_data

    def set_next(self, next_node):
        self.next = next_node

    def get_next(self):
        return self.next

    def get_item(self):
        return self.item


class LinkedList:
    def __init__(self):
        self.head = None

    def __eq__(self, other):
        return self.print_lst() == other.print_lst()

    def is_empty(self):
        return self.head is None

    def add(self, item):
        _temp = Node(item)
        _temp.set_next(self.head)
        self.head = _temp

    def print_lst(self):
        _current = self.head
        _lst = ""
        while _current is not None:
            _lst += "[" + str(_current.get_item()) + "] "
            _current = _current.get_next()
        return _lst.rstrip()

    def reverse(self):
        _current = self.head
        _previous = None
        while _current is not None:
            _temp = _current.get_next()
            _current.set_next(_previous)
            _previous = _current
            _current = _temp
        self.head = _previous

    # ToDo : compare reverse test speed
    #
    # Recursion reverse algorithm
    #
    # def reс_reverse(self, node):
    #     if node.get_next() is None:
    #         self.head = node
    #         return node
    #     new_node = self.reс_reverse(node.get_next())
    #     new_node.set_next(node)
    #     return node
    #
    # def reverse(self):
    #     self.reс_reverse(self.head).set_next(None)

    def size(self):
        _current = self.head
        _size = 0
        while _current is not None:
            _current = _current.get_next()
            _size += 1
        return _size

    def search(self, item):
        """
        Search if the item in the list

        :param item: item to found
        :return: True or False
        """
        _current = self.head
        while _current is not None:
            if _current.get_item() == item:
                return True
            _current = _current.get_next()
        return False

    def remove(self, item):
        """
        Remove the first occurrence of the item from the list

        :param item: item to remove
        :return: True if done or False
        """
        # ToDo : use self.is_empty instead, check for all possibilities

        if self.head is None:
            return False
        elif self.head.get_item() == item:
            self.head = self.head.get_next()
            return True
        _previous = self.head
        _current = self.head.get_next()
        while _current is not None:
            if _current.get_item() == item:
                _previous.set_next(_current.get_next())
                return True
            _previous = _current
            _current = _current.get_next()
        return False

    def append(self, item):
        """
        Add item to the end of the list
        Reverse of 'add'

        :param item: item to add
        :return: None
        """
        # ToDo : modify append method for better speed
        _new_node = Node(item)
        _current = self.head
        while _current.get_next() is not None:
            _current = _current.get_next()
        _current.set_next(_new_node)

    def index(self, item):
        """
        Find position of the item in the list

        :param item: item to found
        :return: item position or False
        """
        _current = self.head
        _count = 0
        while _current is not None:
            if _current.get_item() == item:
                return _count
            _count += 1
            _current = _current.get_next()
        return False

    def insert(self, item, pos):
        """
        Insert item to the given position

        :param item: item to insert
        :param pos: position index
        :return: None
        """
        _current = self.head
        _previous = None
        _new_node = Node(item)
        _count = 0
        if pos == 0:
            _new_node.set_next(_current)
            self.head = _new_node
            return
        while _count != pos:
            _previous = _current
            _current = _current.get_next()
            _count += 1
        _previous.set_next(_new_node)
        _new_node.set_next(_current)
        return

    def pop(self, pos):
        """
        Remove item at the given position

        :param pos: item to remove position
        :return: None
        """

        # ToDo : add default logic for pop method
        _current = self.head
        _previous = None
        _count = 0
        while _count != pos:
            _count += 1
            _previous = _current
            _current = _current.get_next()
        if _previous is None:
            self.head = _current.get_next()
            return
        else:
            _previous.set_next(_current.get_next())
            return
