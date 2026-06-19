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

    # TODO: add get_item_by_name(name: str) -> MenuItem | None — natural
    # lookup helper for validating items before adding them to a Transaction.


if __name__ == "__main__":
    menu = Menu()
    menu.add_item(MenuItem("Latte", 4.50, "Drinks", 4.8))
    menu.add_item(MenuItem("Brownie", 2.75, "Desserts", 4.2))
    menu.add_item(MenuItem("Sandwich", 6.50, "Mains", 4.0))

    customer = Customer("Alex")
    print(f"New user: {customer.name}")
    print(f"verify_user: {customer.verify_user()}")

    order = Transaction()
    order.add_item(menu.items[0])  # Latte
    order.add_item(menu.items[1])  # Brownie
    customer.add_to_history(order)

    print(f"Order: {[i.name for i in order.items]}")
    print(f"Total: ${order.compute_total():.2f}")
    print(f"verify_user after order: {customer.verify_user()}")
