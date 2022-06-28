from abc import ABC, abstractmethod
from typing import Union


class Storage(ABC):
    @abstractmethod
    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, item, qnt) -> Union[dict, int]:
        pass

    @abstractmethod
    def remove(self, item, qnt) -> Union[dict, int]:
        pass

    @property
    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @property
    @abstractmethod
    def items(self) -> dict:
        pass

    @property
    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass




if __name__ == '__main__':
    print("Всего на складе хранится: ", "словарь вещей и к-ва")

    print("Создаём экземпляр класса Goods (пытаемся забрать 4 ед. со склада)")
    python = Store(qnt=4)
    print("Осталось на складе: ", Store.amount)

    print(f"Курьер забирает {python.amount}{product} со склада")

    print("Отгрузили со склада в экземпляр класса:", python.amount)
    print(f"Курьер везет {python.amount}{python.product} со склада")

    print("Отгружаем все имеющиеся товары со склада в экземпляр класса:")
    python.fullfill()
    print("Осталось на складе:", Store.amount)
    print("Имеется в экземпляре:", python.amount)

    print(f"Курьер доставил {python.amount}{python.product} в магазин")
    print("Всего на складе хранится: ", "словарь вещей и к-ва")
