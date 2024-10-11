import pandas as pd
import datetime
from item_data import items
import json

payment_methods = ["cash", "e-money"]
coupon_price = 5000

class Payment:
    def __init__(self, filename="bazar", format="json"):
        self.total = 0
        self.cash = 0
        self.buyer_name = "Nama?"
        self.coupon_count = 0
        self.change = 0
        self.tip = 0
        self.payment_method = 0
        self.purchased_items = []
        self.total_quantity = 0
        self.purchased_iterator = []
        self.filename = filename
        self.format = format
        self.log_data = []
        try:
            with open(self.filename+'.'+self.format.upper(), "r") as f:
                self.log_data = json.load(f)
        except FileNotFoundError:
            self.log_data = []

        # print(self.log_data)

    def getName(self):
        return self.buyer_name

    def getTotal(self):
        return self.total

    def getCash(self):
        return self.cash
    
    def getCoupons(self):
        return self.coupon_count

    def getChange(self):
        return self.change
    
    def getTip(self):
        return self.tip
    
    def getQuantity(self):
        total = 0
        for item in self.purchased_items:
            total += item["quantity"]
        return total

    def setPurchasedItems(self, item_boxes):
        self.purchased_items = [{"item":item_box.item, "quantity":item_box.quantity} for item_box in item_boxes if item_box.quantity > 0]
        purchased_items_id = []
        for item in self.purchased_items:
            temp = item["item"]
            # print(temp)
            purchased_items_id.append(temp.id)
        for i in self.purchased_iterator:
            if not (i in purchased_items_id):
                self.purchased_iterator.remove(i)
        for item_id in purchased_items_id:
            if not ( item_id in self.purchased_iterator ):
                self.purchased_iterator.append(item_id)

        # print("id", purchased_items_id)
        # print("i", self.purchased_iterator)
        # print("")
        
        self.updateTotal()

    def getItemIterator(self):
        return self.purchased_iterator

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
        self.buyer_name = "Nama?"
        self.coupon_count = 0
        self.change = 0
        self.tip = 0
        self.payment_method = 0
        self.purchased_items = []

    def log_payment(self):
        timestamp = datetime.datetime.now()

        log_data = {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_name": self.buyer_name,
            "payment_method": self.payment_method,
            "coupon_count": self.coupon_count,
            "items": [
                {"name": item["item"].name, "price": item["item"].price, "quantity": item["quantity"]}
                for item in self.purchased_items if item["quantity"] > 0
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
            
    def log_data_to_file(self, filename=None, format=None):
        """
        Logs a Python dictionary (`log_data`) into a specified format (JSON, CSV, XLSX) using Pandas.

        Args:
            log_data (dict): The dictionary containing the log information.
            filename (str): The desired filename for the output file (including extension).
            format (str, optional): The format for the output file (default: "json").
                Can be "json", "csv", or "xlsx".

        Raises:
            ValueError: If the provided format is not supported.
        """

        fn = ''
        frmt = ''

        if filename:
            fn = filename
        else:
            fn = self.filename

        if format:
            frmt = format
        else:
            frmt = self.format

        timestamp = datetime.datetime.now()

        self.log_data.append({
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "buyer_name": self.buyer_name,
            "payment_method": self.payment_method,
            "coupon_count": self.coupon_count,
            "cash": self.cash,
            "change": self.change,
            "tip": self.tip,
            "items": [
                {"name": item["item"].name, "price": item["item"].price, "quantity": item["quantity"]}
                for item in self.purchased_items if item["quantity"] > 0
            ]
        })

        df = pd.DataFrame(self.log_data)  # Create a DataFrame from the dictionary

        if frmt.lower() == "json":
            df.to_json(fn+'.'+frmt.upper(), orient="records", indent=2)
        elif frmt.lower() == "csv":
            df.to_csv(fn+'.'+frmt.upper(), index=False)
        elif frmt.lower() == "xlsx":
            df.to_excel(fn+'.'+frmt.upper(), index=False)
        else:
            raise ValueError(f"Unsupported format: {frmt}")

        print(f"Successfully logged data to {fn} in {frmt.upper()} format.")

        # Example usage
        # ... (same as before)