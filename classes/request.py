class Request:
    # from_ = "store_1"
    # to_ = "shop_1"
    # amount = 0
    # product = "Unknown"

    def __init__(self, order):
        self.order = self._order_split(order)
        self.from_ = self.order[4] + " " + self.order[5]
        self.to_ = self.order[7] + " " + self.order[8]
        self.amount = int(self.order[1])
        self.product = self.order[2]

    @staticmethod
    def _order_split(order):
        return order.split(" ")

    # def request(self) -> dict:
        # order_split = self.order.split(" ")
        # order_final = {"from": self.storage, "to": order_split[7] + " " + order_split[8],
        #                "amount": order_split[1], "product": order_split[2]}
        # return order_final

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to_}"
        # return self.request()

# if __name__ == '__main__':
#     storages = ["склад 1", "склад 2"]
#     req_1 = Request(order="Доставить 3 печеньки из склад 2 в магазин 1")
#     print(req_1.__repr__())
