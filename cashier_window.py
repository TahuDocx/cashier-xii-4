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

class InformationPanel:
    def __init__(self, width, height, bgBatch, textBatch):
        self.width = 350
        self.height = height-100
        self.x = width - self.width
        self.y = 0
        self.xLabel = self.x + 20
        self.xInpInf = self.x + 180
        self.xLabel = self.x+20
        self.xInpInf = self.x+180
        self.yLabel = {
            "name": self.height-50,
            "paymentMethod": self.height-90,
            "total": self.height-130,
            "cash": self.height-170,
            "coupons": self.height-210,
            "change": self.height-250,
            "tip": self.height-290,
        }
        self.container = pyglet.shapes.BorderedRectangle(x=width-self.width, y=0, width=self.width, height=height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)

        self.labels = [
            pyglet.text.Label('Name', x=self.xLabel, y=self.yLabel["name"], anchor_y='bottom',
                             color=(255, 255, 255, 255), batch=textBatch),
            pyglet.text.Label('Payment Method', x=self.xLabel, y=self.yLabel["paymentMethod"], anchor_y='bottom',
                             color=(255, 255, 255, 255), batch=textBatch),
            pyglet.text.Label('Total', x=self.xLabel, y=self.yLabel["total"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label('Cash', x=self.xLabel, y=self.yLabel["cash"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label('Coupons', x=self.xLabel, y=self.yLabel["coupons"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label('Change', x=self.xLabel, y=self.yLabel["change"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label('Tip', x=self.xLabel, y=self.yLabel["tip"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch)
        ]

        self.info = [
            pyglet.text.Label(f"{infoPayment.getTotal()}", x=self.xInpInf, y=self.yLabel["total"],
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
            pyglet.text.Label(f"{infoPayment.getChange()}", x=self.xInpInf, y=self.yLabel["change"], 
                             anchor_y='bottom', color=(255, 255, 255, 255),
                             batch=textBatch),
        ]

        self.inputs = [
            TextInput("name", 'Nama?', self.xInpInf, self.yLabel["name"], self.width - 210, textBatch),
            TextInput("cash", '0', self.xInpInf, self.yLabel["cash"], self.width - 210, textBatch),
            TextInput("coupons", '0', self.xInpInf, self.yLabel["coupons"], self.width - 210, textBatch),
            TextInput("tip", '0', self.xInpInf, self.yLabel["tip"], self.width - 210, textBatch),
        ]

    def setInfo(self):
        self.info[0].text = f"{infoPayment.getTotal()}"
        self.info[1].text = f"{infoPayment.getChange()}"

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
    def __init__(self, text, x, y, width, height, batch):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.label = pyglet.text.Label(f"{text}", font_size=14, x=x, y=y, width=width, height=height, align="center", anchor_y="bottom", batch=batch)
        self.rec = pyglet.shapes.BorderedRectangle(x=x, y=y, width=width, height=height, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=batch)

    def updateLabel(self, text):
        self.label.text = text

class ItemBox:
    def __init__(self, item, x, y, bgBatch, textBatch):
        self.item = item
        self.quantity = 0

        self.labels = [
            Label(f"{item.name}", x, y+60, 180, 30, textBatch),
            Label(f"{item.price}", x, y+30, 180, 30, textBatch),
            Label(f"{self.quantity}", x, y, 180, 30, textBatch),
        ]

        self.buttons = [
            Label("+", x+150, y, 30, 30, textBatch),
            Label("-", x+120, y, 30, 30, textBatch),
        ]

        self.container = pyglet.shapes.BorderedRectangle(x=x-10, y=y-10, width=200, height=110, border_color=(255,255,255,255), color=(0,0,255,255), border=2, batch=bgBatch)

    def update_quantity(self):
        self.labels[2].updateLabel(str(self.quantity))
    
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
            ItemBox(item, 100, 500 - i * 120, self.bgBatch, self.textBatch) for i, item in enumerate(item_data.items)
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