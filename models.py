class Customer:
    def __init__(self, name: str):
        self.name = name
        self.purchase_history = []

    def verify_user(self) -> bool:
        # TODO: spec says "verify they are real users" — consider checking
        # that self.name is a non-empty string instead of relying on purchase
        # history, since a brand new customer with no history is still real.
        return len(self.purchase_history) > 0

    def add_to_history(self, transaction):
        self.purchase_history.append(transaction)

    def total_spent(self) -> float:
        return sum(t.compute_total() for t in self.purchase_history)

    def get_history_by_total(self, min_total: float) -> list:
        return [t for t in self.purchase_history if t.compute_total() >= min_total]

    # TODO: add a place_order(transaction: Transaction) method that creates a
    # Transaction, adds items to it, then calls add_to_history — keeps the
    # full ordering workflow in one place instead of leaving it implicit.


class Transaction:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # TODO: validate that `item` exists on the Menu before appending —
        # spec says a customer shouldn't be able to order a non-menu item.
        # Options: pass a Menu reference into Transaction, or validate at the
        # caller (e.g. inside Customer.place_order) before calling add_item.
        self.items.append(item)

    def compute_total(self) -> float:
        return sum(item.price for item in self.items)


class MenuItem:
    def __init__(self, name: str, price: float, category: str, popularity_rating: float):
        # TODO: add validation — negative price or popularity_rating above a
        # sensible max (e.g. 5.0) can silently slip in without guards here.
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def get_details(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "popularity_rating": self.popularity_rating,
        }


class Menu:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        # TODO: guard against duplicate MenuItem names being added — the menu
        # is a catalog, not a cart, so the same item shouldn't appear twice.
        self.items.append(item)

    def filter_by_category(self, category: str) -> list:
        return [item for item in self.items if item.category == category]

    def get_item_by_name(self, name: str):
        return next((item for item in self.items if item.name == name), None)

    def sort_by_price(self, reverse: bool = False) -> list:
        return sorted(self.items, key=lambda i: i.price, reverse=reverse)

    def sort_by_popularity(self, reverse: bool = True) -> list:
        return sorted(self.items, key=lambda i: i.popularity_rating, reverse=reverse)


if __name__ == "__main__":
    menu = Menu()
    menu.add_item(MenuItem("Latte", 4.50, "Drinks", 4.8))
    menu.add_item(MenuItem("Brownie", 2.75, "Desserts", 4.2))
    menu.add_item(MenuItem("Sandwich", 6.50, "Mains", 4.0))

    customer = Customer("Alex")
    print(f"New user: {customer.name}")
    print(f"verify_user: {customer.verify_user()}")

    order1 = Transaction()
    order1.add_item(menu.items[0])  # Latte
    order1.add_item(menu.items[1])  # Brownie
    customer.add_to_history(order1)

    order2 = Transaction()
    order2.add_item(menu.items[2])  # Sandwich
    customer.add_to_history(order2)

    print(f"\nOrder 1: {[i.name for i in order1.items]} — ${order1.compute_total():.2f}")
    print(f"Order 2: {[i.name for i in order2.items]} — ${order2.compute_total():.2f}")
    print(f"verify_user after orders: {customer.verify_user()}")

    print(f"\ntotal_spent: ${customer.total_spent():.2f}")
    big_orders = customer.get_history_by_total(5.00)
    print(f"orders >= $5.00: {len(big_orders)} (totals: {[f'${t.compute_total():.2f}' for t in big_orders]})")

    print(f"\nsort_by_price: {[i.name for i in menu.sort_by_price()]}")
    print(f"sort_by_popularity: {[i.name for i in menu.sort_by_popularity()]}")
    print(f"get_item_by_name('Latte'): {menu.get_item_by_name('Latte').get_details()}")
