class Node:
    def __init__(self, initdata):
        self._data = initdata
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, newdata):
        self._data = newdata

    def set_next(self, newnext):
        self._next = newnext


class UnorderedList:
    def __init__(self):
        self._head = None
        self._end = None

    def is_empty(self):
        return self._head is None

    def add(self, item):
        _temp = Node(item)
        _temp.set_next(self._head)
        self._head = _temp
        if self._end is None:
            self._end = self._head

    def size(self):
        _current = self._head
        _count = 0
        while _current is not None:
            _count += 1
            _current = _current.get_next()
        return _count

    def search(self, item):
        _current = self._head
        _found = False
        while _current is not None and not _found:
            if item == _current.get_data():
                _found = True
            else:
                _current = _current.get_next()
        return _found

    def remove(self, item):
        _current = self._head
        _previous = None
        _found = False
        while not _found:
            if _current.get_data() == item:
                _found = True
            else:
                _previous = _current
                _current = _current.get_next()

        if _previous is None:
            self._head = _current.get_next()
        elif _current.get_next() is None:
            self._end = _previous
            _previous.set_next(_current.get_next())
        else:
            _previous.set_next(_current.get_next())

    def append(self, item):
        _temp = self._end
        self._end = Node(item)
        _temp.set_next(self._end)
