class Shop:
    _small_shop_capacity = 10

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items_count = 0
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return cls(name, type, cls._small_shop_capacity)

    def add_item(self, item_name: str):
        if self.items_count == self.capacity:
            return "Not enough capacity in the shop"

        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.items_count += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name: str, amount: int):
        error_message = f"Cannot remove {amount} {item_name}"
        if item_name not in self.items:
            return error_message
        if self.items[item_name] < amount:
            return error_message
        self.items[item_name] -= amount
        self.items_count -= amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
