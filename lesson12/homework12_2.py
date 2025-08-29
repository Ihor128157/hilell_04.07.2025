class Item:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name}, price: {self.price}"


class User:
    def __init__(self, name, surname, numberphone):
        self.name = name
        self.surname = surname
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname}"


class Purchase:
    def __init__(self, user):
        self.products = {}  # {Item: quantity}
        self.user = user

    def add_item(self, item, cnt):
        self.products[item] = cnt  # перезаписує кількість

    def get_total(self):
        return sum(item.price * qty for item, qty in self.products.items())

    def __str__(self):
        lines = [f"User: {self.user}", "Items:"]
        for item, qty in self.products.items():
            lines.append(f"{item.name}: {qty} pcs.")
        return '\n'.join(lines)


# --- Тестування ---
lemon = Item('lemon', 5, "yellow", "small")
apple = Item('apple', 2, "red", "middle")
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""

assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'

# Оновимо кількість яблук
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

assert cart.get_total() == 40, 'Повинно залишатися 40!'
