class Item(object):
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value

    def __str__(self):
        return f"Item: {self.value}"


class Deque(object):
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push_right(self, item):
        self.size += 1
        if self.tail is None:
            tmp = Item(item)
            self.head = tmp
            self.tail = tmp
        else:
            tmp_item = Item(item)
            tmp_item.prev = self.tail
            self.tail.next = tmp_item
            self.tail = tmp_item

    def push_left(self, item):
        self.size += 1
        if self.head is None:
            tmp = Item(item)
            self.head = tmp
            self.tail = tmp
        else:
            tmp_item = Item(item)
            tmp_item.next = self.head
            self.head.prev = tmp_item
            self.head = tmp_item

    def pop_left(self):
        if self.head is not None:
            self.size -= 1
            old = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return old.value
        return None

    def pop_right(self):
        if self.tail is not None:
            self.size -= 1
            old = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return old.value
        return None

    def __len__(self):
        return self.size

    def __str__(self):
        return f"size is {self.size} head is {self.head} tail is {self.tail}"


def test_deque():
    deque = Deque()
    deque.push_left(1)
    deque.push_right(2)
    assert len(deque) == 2
    assert deque.pop_right() == 2
    assert deque.pop_left() == 1
    assert deque.pop_left() is None
    assert deque.pop_right() is None
    deque.push_left(1)
    deque.push_left(2)
    assert len(deque) == 2
    assert deque.pop_right() == 1
    assert deque.pop_right() == 2
    assert len(deque) == 0
    assert deque.pop_left() is None
    assert deque.pop_right() is None
    deque.push_left(1)
    deque.push_left(2)
    deque.push_right(3)
    assert len(deque) == 3
    assert deque.pop_right() == 3
    assert deque.pop_right() == 1
    assert deque.pop_right() == 2
    assert len(deque) == 0
    assert deque.pop_left() is None
    assert deque.pop_right() is None
    deque.push_left(1)
    deque.push_left(2)
    deque.push_right(3)
    assert len(deque) == 3
    assert deque.pop_left() == 2
    assert deque.pop_left() == 1
    assert deque.pop_left() == 3
    assert len(deque) == 0
    assert deque.pop_left() is None
    assert deque.pop_right() is None


if __name__ == "__main__":
    test_deque()
    print("Ok")
