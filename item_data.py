CATEGORIES = ["Makanan Berat", "Makanan Ringan", "Minuman"]

class Item:
    def __init__(self, category, idNum, name, price, image_source=None, desc=None):
        self.category = CATEGORIES[category]
        self.id = idNum
        self.name = name
        self.desc = desc
        self.price = price
        self.image_path = image_source
        self.quantity = 0

# items = [
#     Item(0, 1, "Item 1", 10000),
#     Item(0, 2, "Item 2", 15000),
#     Item(0, 3, "Item 3", 10000),
#     Item(0, 4, "Item 4", 15000),
#     Item(0, 5, "Item 5", 10000),
#     Item(0, 6, "Item 6", 15000),
#     Item(0, 7, "Item 7", 15000),
#     Item(0, 8, "Item 8", 10000),
#     Item(0, 9, "Item 9", 15000),
#     # Add more items here
# ]

items = [
    Item(0, i+1, f"Item {i+1}", (i+1)/2*10000) for i in range(21)
]

# Function to get item by ID (optional)
def get_item_by_id(item_id):
    for item in items:
        if item.id == item_id:
            return item
    return None