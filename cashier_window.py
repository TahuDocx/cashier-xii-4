import pyglet
from pyglet.window import Window
import pyglet.text.caret
import item_data
import pyglet.text.layout
from payment import Payment
import datetime
# from main import buyer_window
from title import Title

infoPayment = Payment()

class PurchasedItems:
    def __init__(self):
        pass

class InformationPanel:
    def __init__(self, width, height, bgBatch, textBatch):
        self.width = 500
        self.height = 414
        self.x = width - self.width
        self.y = 0
        self.xLabel = self.x + 24
        self.xInpInf = self.x + 202
        self.iGapY = -1

        
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
        self.container = pyglet.shapes.BorderedRectangle(x=width-self.width, y=0, width=self.width, height=self.height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)

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
            pyglet.text.Label(f"{infoPayment.getTotal()}", x=self.xInpInf, y=self.yLabel["total"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getQuantity()}", x=self.xInpInf, y=self.yLabel["total_quantity"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getChange()}", x=self.xInpInf, y=self.yLabel["change"], 
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
        ]

        self.inputs = [
            TextInput("name", 'Nama?', self.xInpInf, self.yLabel["name"], 274, textBatch),
            TextInput("cash", '0', self.xInpInf, self.yLabel["cash"], 274, textBatch),
            TextInput("coupons", '0', self.xInpInf, self.yLabel["coupons"], 274, textBatch),
            TextInput("tip", '0', self.xInpInf, self.yLabel["tip"], 274, textBatch),
        ]

    def setInfo(self):
        self.info[0].text = f"{infoPayment.getTotal()}"
        self.info[1].text = f"{infoPayment.getQuantity()}"
        self.info[2].text = f"{infoPayment.getChange()}"

    def gap(self):
        inGap = 50
        gap = 35
        self.iGapY += 1
        return inGap + gap * self.iGapY
    # def resetInfo(self):


class TextInput:
    def __init__(self, name, text, x, y, width, batch):
        self.name = name
        self.document = pyglet.text.document.UnformattedDocument(text)
        self.document.set_style(0, len(self.document.text), dict(color=(255, 255, 255, 255), underline=(255, 255, 255, 255)))
        font = self.document.get_font()
        height = font.ascent - font.descent

        self.layout = pyglet.text.layout.IncrementalTextLayout(self.document, width, height, batch=batch)
        self.layout.position = x, y, 0
        self.caret = pyglet.text.caret.Caret(self.layout)
        # Rectangular outline
        pad = 2
        self.rectangle = pyglet.shapes.Rectangle(x=x - pad, y=y - pad, width=width + pad, height=height + pad, color=(200, 200, 220, 100), batch=batch)

    def hit_test(self, x, y):
        return (0 < x - self.layout.x < self.layout.width and
                0 < y - self.layout.y < self.layout.height)

    def get_text(self):
        return self.document.text
    
    def get_number(self):
        if self.document.text == '':
            return 0
        return int(self.document.text)

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

class Button:
    def __init__(self, text, x, y, width, height, batch, font_size=14, bold=False, italic=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = pyglet.text.Label(f"{text}", font_size=font_size, x=x, y=y, width=width, height=height, anchor_y="bottom", align="center", bold=bold, italic=italic, batch=batch)
        self.rec = pyglet.shapes.BorderedRectangle(x=x, y=y, width=width, height=height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=batch)

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
            "quantity": 32
        }
        quantityWidth = 124
        xLabel = x+169
        yLabel = {
            "category": y+135,
            "name": y+113,
            "desc": y+86,
            "price":y+64,
            "quantity": y+24
        }

        self.labels = [
            Label(f"{item.category}", xLabel, yLabel["category"], labelWidth, labelHeight["category"], textBatch, 8, True),
            Label(f"{item.name}", xLabel, yLabel["name"], labelWidth, labelHeight["name"], textBatch, 12, True),
            # Label(f"{item.desc}", xLabel, yLabel["desc"], labelWidth, labelHeight["name"], textBatch, 8, True),
            Label(f"{item.price}", xLabel, yLabel["price"], labelWidth, labelHeight["price"], textBatch, 12),
            Label(f"{self.quantity}", xLabel, yLabel["quantity"], quantityWidth, labelHeight["quantity"], textBatch, 17, container=True, align="center"),
        ]

        self.buttons = [
            Button("+", x+150, y, 30, 30, textBatch),
            Button("-", x+120, y, 30, 30, textBatch),
        ]

        # self.image = pyglet.image.load(self.item.image_path)
        self.image = pyglet.shapes.Rectangle(x=x+12, y=y+12, width=144, height=144, color=(0,150,255), batch=textBatch)

        self.container = pyglet.shapes.BorderedRectangle(x=x, y=y, width=self.width, height=self.height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)

    def update_quantity(self):
        self.labels[3].updateLabel(str(self.quantity))
    
    def get_quantity(self):
        return int(self.quantity_label.text)
    
    def click(self, x, y):
        if self.buttons[0].x <= x <= self.buttons[0].x + self.buttons[0].width and \
            self.buttons[0].y <= y <= self.buttons[0].y + self.buttons[0].height:
                self.quantity += 1
                self.update_quantity()
        elif self.buttons[1].x <= x <= self.buttons[1].x + self.buttons[1].width and \
            self.buttons[1].y <= y <= self.buttons[1].y + self.buttons[1].height:
            self.quantity = max(0, self.quantity - 1)
            self.update_quantity()

class CashierWindow(Window):
    def __init__(self, buyer):
        super().__init__(width=1920, height=1009, caption="Cashier", resizable=True)
        self.maximize()  # Maximize the window on creation
        self.set_minimum_size(1920, 1009)
        self.set_maximum_size(1920, 1009)

        pyglet.gl.glClearColor(0.0, 0.0, 0.7, 1.0)

        self.bgBatch = pyglet.graphics.Batch()
        self.textBatch = pyglet.graphics.Batch()

        self.header = Title(1920, 1009, self.textBatch)
        
        self.text_cursor = self.get_system_mouse_cursor('text')

        self.payment_methods = ["Cash", "E-Money"]
        self.payment_method = "Cash"
        self.item_boxes = [
            ItemBox(item, 100, 500 - i * 223, self.bgBatch, self.textBatch) for i, item in enumerate(item_data.items)
        ]

        self.infoPanel = InformationPanel(self.width, self.height, self.bgBatch, self.textBatch)

        self.focus = None
        self.set_focus(self.infoPanel.inputs[0])
        # self.test = pyglet.shapes.Rectangle(0,0,1920,71,(255,255,255))

        self.buyer_window = buyer

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.windowSize = self.get_size()
        # self.infoPanel.resize(self.windowSize[0], self.windowSize[1])
        # print(self.windowSize)
        # self.infoPanel.update(self.windowSize[0], self.windowSize[1])

    def on_draw(self):
        # pyglet.gl.glClearColor(1, 1, 1, 1)
        self.clear()
        self.bgBatch.draw()
        self.textBatch.draw()
        # self.test.draw()
        # for item_box in self.item_boxes:
            # item_box.draw()
        # self.infoPanel.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        for input in self.infoPanel.inputs:
            if input.hit_test(x, y):
                self.set_mouse_cursor(self.text_cursor)
                break
        else:
            self.set_mouse_cursor(None)

    def on_mouse_press(self, x, y, button, modifiers):
        for input in self.infoPanel.inputs:
            if input.hit_test(x, y):
                self.set_focus(input)
                break
            else:
                self.set_focus(None)
        
        for item_box in self.item_boxes:
            item_box.click(x,y)
            infoPayment.setPurchasedItems(self.item_boxes)
            self.infoPanel.setInfo()
            self.buyer_window.update(infoPayment.getPurchasedItems())


    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.focus:
            self.focus.caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_text(self, text):
        if self.focus:
            self.focus.caret.on_text(text)

    def on_text_motion(self, motion):
        if self.focus:
            self.focus.caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self.focus:
            self.focus.caret.on_text_motion_select(motion)

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.TAB:
            if modifiers & pyglet.window.key.MOD_SHIFT:
                direction = -1
            else:
                direction = 1

            if self.focus in self.infoPanel.inputs:
                i = self.infoPanel.inputs.index(self.focus)
            else:
                i = 0
                direction = 0

            self.set_focus(self.infoPanel.inputs[(i + direction) % len(self.infoPanel.inputs)])

        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()
        

    def on_key_release(self, symbol, modifiers):
        inputs = self.infoPanel.inputs

        infoPayment.updateName(inputs[0].get_text())
        infoPayment.updateCash(inputs[1].get_number(), inputs[2].get_number(), inputs[3].get_number())
        self.infoPanel.setInfo()

    def set_focus(self, focus):
        if focus is self.focus:
            return

        if self.focus:
            self.focus.caret.visible = False
            self.focus.caret.mark = self.focus.caret.position = 0

        self.focus = focus
        if self.focus:
            self.focus.caret.visible = True