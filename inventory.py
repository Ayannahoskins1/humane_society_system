class InventoryItem:
    def __init__(self, item_id, name, quantity, unit, category):
        self.item_id = item_id
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category

    def update_quantity(self, amount):
        self.quantity += amount

    def __str__(self):
        return f"{self.item_id}: {self.name} ({self.quantity} {self.unit}) - {self.category}"
