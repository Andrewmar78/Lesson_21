from typing import Union
from classes.storage import Storage


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, item, qnt):
        if item in self._items:
            self._items[item] += qnt
        else:
            self._items[item] = qnt
        self._capacity -= qnt

    def remove(self, item, qnt):
        rest = self._items[item] - qnt
        if rest > 0:
            self._items[item] = rest
        else:
            del self._items[item]
        self._capacity += qnt

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        capacity_hold = sum(self._items.values())
        self._capacity -= capacity_hold

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())
