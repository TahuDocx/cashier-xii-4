CATEGORIES = ["Makanan Berat", "Makanan Ringan", "Minuman"]

class Item:
    # def __init__(self, category, id, name, desc, price, image_source=""):
    def __init__(self, category, id, name, price, image_source=""):
        self.category = CATEGORIES[category]
        self.id = id
        self.name = name
        # self.desc = desc
        self.price = price
        self.image_path = image_source
        # self.quantity = 0

items = [
    Item(0, 1, "Item 1", 10000),
    Item(0, 2, "Item 2", 15000),
    # Add more items here
]

# Function to get item by ID (optional)
def get_item_by_id(item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None