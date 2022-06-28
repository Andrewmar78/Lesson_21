from classes.request import Request

# Исходные данные
from classes.shop import Shop
from classes.store import Store

storages = ["склад 1", "склад 2"]
storages_capacity = 100
shops = ["магазин 1", "магазин 2"]
shops_capacity = 20

# items = {
#     storages[0]: {
#         "печеньки": 10, "конфетки": 10, "ватрушки": 10, "пастилки": 10, "ириски": 10},
#     storages[1]: {
#         "печеньки": 20, "конфетки": 20, "ватрушки": 20, "пастилки": 20, "ириски": 20}
# }


def main():
    # item = "ириски"
    # amount = 1
    # transfer_from = storages[0]
    # transfer_to = shops[0]
    #
    # order = f"Доставить {amount} {item} из {transfer_from} в {transfer_to}"
    # print(order)
    # store = Store()
    # shop = Shop()
    # request = Request(order)

    store_items = {
        "печеньки": 10, "конфетки": 8, "зефирки": 6, "пастилки": 4, "ириски": 2
    }

    while True:
        item = input("Введите товар для перемещения\n")
        amount = input("Введите количество товара\n")
        # transfer_from = input("Откуда везти товар?\n")
        # transfer_to = input("Куда везти товар?\n")
        transfer_from = storages[0]
        transfer_to = shops[0]

        order = f"Доставить {amount} {item} из {transfer_from} в {transfer_to}"
        print(order)
        store = Store()
        shop = Shop()
        request = Request(order)

        if item == "stop":
            break

        store.items = store_items

        if request.from_ in storages:
            transfer_from = store
            transfer_to = shop
        elif request.from_ in shops:
            transfer_from = shop
            transfer_to = store
        # else:
        #     transfer_from = None
        #     transfer_to = None

        transfer = []

        if request.product in transfer_from.items:
            print(f"Такой товар есть в {request.from_} в количестве {store.items[request.product]}")
        else:
            print(f"Такого товара нет в {request.from_}")
            transfer.append(False)
            continue

        if transfer_from.items[request.product] >= request.amount:
            print(f"Такое количество товара есть на {request.from_}")
        else:
            print(f'Не хватает {request.amount - transfer_from.items[request.product]} {request.product} на складе,'
                  f' попробуйте заказать меньше')
            transfer.append(False)
            continue

        if transfer_to.get_free_space >= request.amount:
            print(f"Места в {request.to_} достаточно")
        else:
            print(f"В {request.to_} не хватает {request.amount - transfer_to.get_free_space} места,"
                  f" уменьшите количество товара")
            transfer.append(False)
            continue

        # print("?" * 20)
        # print(request.to_)
        # print(transfer_to)
        # print(transfer_to.get_unique_items_count)
        # print(request.product)
        # print(transfer_to.items)
        # print("?" * 20)

        if request.to_ in shops and (transfer_to.get_unique_items_count != 0 or request.product in transfer_to.items):
            print("В магазине хватает уникальных товаров")
        else:
            print("В магазине не хватает уникальных товаров")

        # print(transfer)
        if False not in transfer:
            transfer_from.remove(request.product, request.amount)
            print("-" * 20)
            print(f"Курьер забрал {request.amount} {request.product} из {request.from_}")
            print(f"Курьер везет {request.amount} {request.product} из {request.from_} в {request.to_}")
            transfer_to.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в {request.to_}")
            print("-"*20)
            print(f"В {request.from_} осталось:")
            for product, qnt in transfer_from.items.items():
                print(f"{product}: {qnt}")
            print(f"Свободного места осталось {store.get_free_space}")
            print("-" * 20)
            print(f"В {request.to_} теперь:")
            for product, qnt in transfer_to.items.items():
                print(f"{product}: {qnt}")
            print(f"Свободного места осталось {shop.get_free_space}")
        else:
            print("Что-то пошло не так")
        # break


if __name__ == '__main__':
    main()
