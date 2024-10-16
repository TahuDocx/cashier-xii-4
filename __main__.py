from cashier_window import CashierWindow
from buyer_window import BuyerWindow
import pyglet

def main():
    cashier_window = CashierWindow()
    buyer_window = BuyerWindow()

    def update(dt):
        buyer_window.update()
        cashier_window.header.clock.update()
    
    pyglet.clock.schedule_interval(update, 1/60.0)  # Update every 60th of a second
    # pyglet.clock.schedule_interval(update, 2)  # Update every 2 seconds

    pyglet.app.run()

if __name__ == "__main__":
    main()