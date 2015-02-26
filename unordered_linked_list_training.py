class Node:
    def __init__(self, init_data):
        self.item = init_data
        self.next = None

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

    def is_empty(self):
        return self.head is None

    def add(self, item):
        _temp = Node(item)
        _temp.set_next(self.head)
        self.head = _temp

    def print(self):
        _current = self.head
        while _current is not None:
            print("[" + str(_current.get_item()) + "]")
            _current = _current.get_next()

    def reverse(self):
        _current = self.head
        _previous = None
        while _current is not None:
            _temp = _current.get_next()
            _current.set_next(_previous)
            _previous = _current
            _current = _temp
        self.head = _previous

    def size(self):
        _current = self.head
        _size = 0
        while _current is not None:
            _current = _current.get_next()
            _size += 1
        return _size

    def search(self, item):
        _current = self.head
        while _current is not None:
            if _current.get_item() == item:
                return True
            _current = _current.get_next()
        return False

    def remove(self, item):
        if self.head.get_item() == item:
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
        # ToDo : fix to better speed
        _new_node = Node(item)
        _current = self.head
        while _current.get_next() is not None:
            _current = _current.get_next()
        _current.set_next(_new_node)

    def index(self, item):
        _current = self.head
        _count = 0
        while _current is not None:
            if _current.get_item() == item:
                return _count
            _count += 1
            _current = _current.get_next()
        return False

    def insert(self, item, pos):
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

    def pop(self, pos):
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
