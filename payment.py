import pandas as pd
import datetime
from item_data import items

payment_methods = ["cash", "e-money"]
coupon_price = 5000

class Payment:
    def __init__(self):
        self.total = 0
        self.cash = 0
        self.buyer_name = "Nama?"
        self.coupon_count = 0
        self.change = 0
        self.tip = 0
        self.payment_method = 0
        self.purchased_items = []
        self.total_quantity = 0

    def getTotal(self):
        return self.total

    def getChange(self):
        return  self.change
    
    def getQuantity(self):
        total = 0
        for item in self.purchased_items:
            total += item["quantity"]
        return total

    def setPurchasedItems(self, item_boxes):
        self.purchased_items = [{"item":item_box.item, "quantity":item_box.quantity} for item_box in item_boxes if item_box.quantity > 0]
        self.updateTotal()

    def getPurchasedItems(self):
        return self.purchased_items

    def updateName(self, name):
        self.buyer_name = name

    def updateTotal(self):
        self.total = 0
        self.total_quantity = 0
        for item in self.purchased_items:
            self.total += item["quantity"] * item["item"].price
            self.total_quantity += item["quantity"]
        self.updateChange()

    def updateCash(self, cash, coupon_count, tip):
        self.cash = cash
        self.coupon_count = coupon_count
        self.tip = tip
        self.updateChange()

    def updateChange(self):
        self.change = (self.cash + coupon_price * self.coupon_count) - self.total

    def reset(self):
        self.total = 0
        self.cash = 0
        self.buyer_name = "Mama?"
        self.coupon_count = 0
        self.change = 0
        self.tip = 0
        self.payment_method = 0
        self.purchased_items = []

    def log_payment(buyer_name, payment_method, coupon_count, purchased_items):
        timestamp = datetime.datetime.now()

        log_data = {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_name": buyer_name,
            "payment_method": payment_method,
            "coupon_count": coupon_count,
            "items": [
                {"name": item.name, "price": item.price, "quantity": item.quantity}
                for item in purchased_items if item.quantity > 0
            ]
        }

        # Convert log data to a DataFrame
        df = pd.DataFrame([log_data])

        # Append to CSV or XLSX file
        try:
            df.to_csv("payment_log.csv", mode='a', header=False, index=False)
        except FileNotFoundError:
            df.to_csv("payment_log.csv", index=False)

        # Optionally, save as XLSX
        # df.to_excel("payment_log.xlsx", index=False)