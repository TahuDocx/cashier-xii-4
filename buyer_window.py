import pyglet
from pyglet.window import Window
from title import Title
from cashier_window import infoPayment, item_boxes
import item_data

items = item_boxes

display = pyglet.canvas.get_display()
screens = display.get_screens()

item_boxes = []

screen = 0
fs = False
width = 1920
height = 1080

if(screens.__len__()>1):
    screen = screens[1]
    fs = True
else:
    height = 1009
    screen = screens[0]
# print(screens)

class PurchasedItemBox:
    def __init__(self, item, x=0, y=0, width=472, height=47, batch=None):
        self.height = height
        self.width = width
        self.item = item
        self.x = x
        self.y = y
        self.label_height = 15
        self.batch = batch
        self.yQty = self.y
        self.yName = self.y
        self.yTotal = self.y

        # print(self.item.quantity)

        self.container = pyglet.shapes.RoundedRectangle(
            x=self.x, y=self.y, width=self.width, height=self.height, color=(0,0,255,255), radius=8, segments=12, batch=self.batch
            )
        self.qty = pyglet.text.Label(
            f"{self.item.quantity}", x=self.x+16, y=self.y, width=27, height=self.label_height, align="center", batch=self.batch
            )
        self.name = pyglet.text.Label(
            self.item.item.name + f"   @Rp {self.item.item.price}", x=self.x+63, y=self.y, height=self.label_height, batch=self.batch
            )
        self.total = pyglet.text.Label(
            f"Rp {self.item.item.price * self.item.quantity}", x=self.x+336, y=self.yTotal, height=self.label_height, batch=self.batch, width=120, align="right"
            )
        self.batch.draw()
        self.clear()
        # self.visibility(False)

    def clear(self):
        self.y = -100
        self.yQty = self.y+16
        self.yName = self.y+16
        self.yTotal = self.y+16

        self.container.y = self.y
        self.qty.y = self.yQty
        self.name.y = self.yName
        self.total.y = self.yTotal

        self.qty.text = str(self.item.quantity)
        self.total.text = "Rp " + str(self.item.item.price * self.item.quantity)
        # print("halo")

    def updateY(self, y):
        # print(y)
        self.y = y
        self.yQty = self.y+16
        self.yName = self.y+16
        self.yTotal = self.y+16

        self.container.y = self.y
        self.qty.y = self.yQty
        self.name.y = self.yName
        self.total.y = self.yTotal
        
        self.qty.text = str(self.item.quantity)
        self.total.text = "Rp " + str(self.item.item.price * self.item.quantity)
        # print("hai")
        # self.visibility(True)

class PurchasedItems:
    def __init__(self, x, y, batch=None):
        self.x = x
        self.initY = y
        self.yGap = 65
        self.boxes = [
            PurchasedItemBox(item, self.x, self.initY + i*self.yGap, batch=batch) for i, item in enumerate(items)
        ]
        # print(self.boxes)

    def update(self):
        iterator = infoPayment.getItemIterator()
        # print("a", iterator)
        for i, item_id in enumerate(iterator):
            for box in self.boxes:
                if box.item.item.id == item_id:
                    # print("t", box.item.item.id, iterator, item_id)
                    box.updateY(self.initY - i*self.yGap)
                elif not (box.item.item.id in iterator):
                    # print("f", box.item.item.id, iterator, item_id)
                    box.clear()

        if not iterator :
            for box in self.boxes:
                box.clear()
        
class InformationPanel:
    def __init__(self, width, height, bgBatch, textBatch):
        self.width = 500
        self.height = 325
        self.x = width - self.width
        self.y = 0
        self.xLabel = self.x + 24
        self.xInpInf = self.x + 202
        self.iGapY = -1

        self.purchased_items = PurchasedItems(self.x+14, 831, textBatch)
        
        self.yLabel = {
            "name": self.height-(self.gap()),
            "payment_method": self.height-(self.gap()),
            "total": self.height-(self.gap()),
            "total_quantity": self.height-(self.gap()),
            "cash": self.height-(self.gap()),
            "coupons": self.height-(self.gap()),
            "change": self.height-(self.gap()),
            "tip": self.height-(self.gap())
        }
        # self.container = pyglet.shapes.BorderedRectangle(x=width-self.width, y=0, width=self.width, height=self.height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)
        self.container = pyglet.shapes.RoundedRectangle(x=width-self.width, y=0, width=self.width, height=self.height, color=(0,0,255,255), batch=bgBatch, radius=(0, 8, 0, 0), segments=8)

        self.labels = [
            pyglet.text.Label('Name', x=self.xLabel, y=self.yLabel["name"], anchor_y='bottom',
                             color=(255, 255, 255, 255), height=24, align="center", font_size=14, batch=textBatch),
            pyglet.text.Label('Payment Method', x=self.xLabel, y=self.yLabel["payment_method"], anchor_y='bottom',
                             color=(255, 255, 255, 255), height=24, align="center", font_size=14, batch=textBatch),
            pyglet.text.Label('Total', x=self.xLabel, y=self.yLabel["total"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch),
            pyglet.text.Label('Total Quantity', x=self.xLabel, y=self.yLabel["total_quantity"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch),
            pyglet.text.Label('Cash', x=self.xLabel, y=self.yLabel["cash"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch),
            pyglet.text.Label('Coupons', x=self.xLabel, y=self.yLabel["coupons"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch),
            pyglet.text.Label('Change', x=self.xLabel, y=self.yLabel["change"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch),
            pyglet.text.Label('Tip', x=self.xLabel, y=self.yLabel["tip"],
                             anchor_y='bottom', color=(255, 255, 255, 255), height=24, align="center", font_size=14,
                             batch=textBatch)
        ]

        self.info = [
            pyglet.text.Label(f"{infoPayment.getName()}", x=self.xInpInf, y=self.yLabel["name"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getTotal()}", x=self.xInpInf, y=self.yLabel["total"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getQuantity()}", x=self.xInpInf, y=self.yLabel["total_quantity"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getCash()}", x=self.xInpInf, y=self.yLabel["cash"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getCoupons()}", x=self.xInpInf, y=self.yLabel["coupons"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getChange()}", x=self.xInpInf, y=self.yLabel["change"], 
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getTip()}", x=self.xInpInf, y=self.yLabel["tip"], 
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
        ]

    def setInfo(self):
        self.info[0].text = f"{infoPayment.getName()}"
        self.info[1].text = f"{infoPayment.getTotal()}"
        self.info[2].text = f"{infoPayment.getQuantity()}"
        self.info[3].text = f"{infoPayment.getCash()}"
        self.info[4].text = f"{infoPayment.getCoupons()}"
        self.info[5].text = f"{infoPayment.getChange()}"
        self.info[6].text = f"{infoPayment.getTip()}"
        self.purchased_items.update()

    def gap(self):
        inGap = 50
        gap = 35
        self.iGapY += 1
        return inGap + gap * self.iGapY
    # def resetInfo(self):

class Label:
    def __init__(self, text, x, y, width, height, batch, font_size=14, isBold=False, isItalic=False, container=False, align="left"):
        self.x = x
        self.y = y
        # self.width = width
        self.height = height
        self.align = align
        self.width = None
        if(container):
            self.width = width
            self.align = "center"
            self.container = pyglet.shapes.BorderedRectangle(x=x, y=y, width=width, height=height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=batch)

        self.label = pyglet.text.Label(f"{text}", font_size=font_size, x=x, y=y, width=self.width, height=self.height, anchor_y="bottom", bold=isBold, italic=isItalic, batch=batch, align=self.align)

    def updateLabel(self, text):
        self.label.text = text

class ItemBox:
    def __init__(self, item, x, y, bgBatch, textBatch):
        self.item = item
        self.quantity = 0
        self.width = 380
        self.height = 168
        labelWidth = 200
        labelHeight = {
            "category": 10,
            "name": 15,
            "desc": 20,
            "price": 15,
        }
        quantityWidth = 124
        xLabel = x+169
        yLabel = {
            "category": y+111,
            "name": y+89,
            "desc": y+62,
            "price": y+40,
        }

        self.labels = [
            Label(f"{item.category}", xLabel, yLabel["category"], labelWidth, labelHeight["category"], textBatch, 8, True),
            Label(f"{item.name}", xLabel, yLabel["name"], labelWidth, labelHeight["name"], textBatch, 12, True),
            # Label(f"{item.desc}", xLabel, yLabel["desc"], labelWidth, labelHeight["name"], textBatch, 8, True),
            Label(f"{item.price}", xLabel, yLabel["price"], labelWidth, labelHeight["price"], textBatch, 12),
        ]

        if self.item.image_path:
            self.image = pyglet.image.load(self.item.image_path)
        else:
            self.image = pyglet.shapes.Rectangle(x=x+12, y=y+12, width=144, height=144, color=(0,150,255), batch=textBatch)

        self.container = pyglet.shapes.BorderedRectangle(x=x, y=y, width=self.width, height=self.height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)

class BuyerWindow(Window):
    def __init__(self):
        super().__init__(caption="Buyer", screen=screen, fullscreen=fs, resizable=not fs, width=width, height=height)

        if not fs:
           self.maximize()  # Maximize the window on creation

        self.set_minimum_size(width, height)
        self.set_maximum_size(width, height)

        pyglet.gl.glClearColor(0.0, 0.0, 0.7, 1.0)

        self.bgBatch = pyglet.graphics.Batch()
        self.textBatch = pyglet.graphics.Batch()
        self.header = Title(width, height, self.textBatch)

        self.infoPanel = InformationPanel(self.width, self.height, self.bgBatch, self.textBatch)


        self.xItemBox = 80
        self.xGapItemBox = 420
        self.yItemBox = 633
        self.yGapItemBox = 223

        i = 0
        j = 0

        for item in item_data.items:
            item_boxes.append(ItemBox(item, self.xItemBox + i*self.xGapItemBox, self.yItemBox - j*self.yGapItemBox, self.bgBatch, self.textBatch))
            i += 1
            if i == 3:
                j += 1
                i = 0
        # Create labels and text fields to display information
        # ...

    def on_draw(self):
        BuyerWindow.clear()
        self.bgBatch.draw()
        self.textBatch.draw()
        # Draw the window contents
        # ...

    def update(self):
        self.header.clock.update()
        self.infoPanel.setInfo()
        # print("u")