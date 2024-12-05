from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.metrics import dp

Window.size = (350,600)

class Myapp(MDApp):
    def build(self):
        return
    def get_number_of_columns(self):
        # Dynamically set the number of columns based on screen width
        width = Window.size[0]
        if width < dp(400):  # Small screens (like mobile)
            return 1
        elif width < dp(800):  # Medium screens (like tablets)
            return 2
        else:  # Large screens (like desktops)
            return 3

Myapp().run()    