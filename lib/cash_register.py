#!/usr/bin/env python3

class CashRegister:
  def _init_(self):
        self.total = 0
        self.items = []
        self.discount = 0
        self.last_transaction = 0

    def add_item(self, item, price):
        self.items.append(item)
        self.total += price
        self.last_transaction = price

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            return f"Discount applied: ${discount_amount:.2f}"
        else:
            return "No discount applied."

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction
            self.items.pop()
            self.last_transaction = 0
        else:
            return "No items to void."

    def get_total(self):
        return f"Total: ${self.total:.2f}"

    def get_items(self):
        return self.items

