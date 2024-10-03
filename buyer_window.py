import pyglet
from pyglet.window import Window
from title import Title

display = pyglet.canvas.get_display()
screens = display.get_screens()

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

        self.items_purchased = []


        # Create labels and text fields to display information
        # ...

    def on_draw(self):
        BuyerWindow.clear()
        self.bgBatch.draw()
        self.textBatch.draw()
        # Draw the window contents
        # ...

    def update(self, purchasedItem):
        self.items_purchased = purchasedItem
        print(self.items_purchased)
        