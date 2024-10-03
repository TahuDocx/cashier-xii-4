class Item:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
        # self.quantity = 0

items = [
    Item(1, "Item 1", 10000.00),
    Item(2, "Item 2", 15000.00),
    # Add more items here
]

# Function to get item by ID (optional)
def get_item_by_id(item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None