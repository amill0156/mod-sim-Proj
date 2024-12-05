class Clubhouse:

    def __init__(self, carts, taken_carts = []):
        self.carts = carts
        self.taken_carts = taken_carts

    def add_cart(self, cart_to_add):
        self.carts.append(cart_to_add)

    def remove_cart(self, cart_to_remove):
        self.carts.remove(cart_to_remove)
        self.taken_carts.append(cart_to_remove)