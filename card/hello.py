from kivy.metrics import dp
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
MDScreen:
    MDScrollView:
        MDGridLayout:
            id: grid
            cols: app.get_number_of_columns()  # Call the method to get the number of columns
            padding: dp(10)
            spacing: dp(10)
            adaptive_height: True

    MDRaisedButton:
        text: "Add Card"
        size_hint: None, None
        size: dp(100), dp(50)
        pos_hint: {"center_x": .5, "y": 0}
        on_release: app.add_card()  # Add this line to call the add_card method
'''

class ResponsiveApp(MDApp):
    def build(self):
        # Bind the window size to update the grid layout on resize
        Window.bind(size=self.on_window_size)
        self.grid = Builder.load_string(kv)
        self.update_columns(Window.size[0])  # Initial column setup
        return self.grid

    def on_window_size(self, window, size):
        self.update_columns(size[0])

    def update_columns(self, width):
        # Update the number of columns based on the window width
        self.grid.ids.grid.cols = self.get_number_of_columns()

    def get_number_of_columns(self):
        # Return the number of columns based on window width
        width = Window.size[0]
        if width < dp(400):  # Small screens (like mobile)
            return 1
        elif width < dp(800):  # Medium screens (like tablets)
            return 2
        else:  # Large screens (like desktops)
            return 3

    def add_card(self):
    # Create a new card and add it to the grid
        card = Builder.load_string('''
        MDCard:
            size_hint: (.45, None)
            height: dp(250)
            elevation: 2
            radius: [dp(15), dp(15), dp(15), dp(15)]
            MDBoxLayout:
                orientation: 'vertical'
                padding: 0
                spacing: 0
                FitImage:
                    source: 'back.jpg'
                    size_hint_y: None
                    height: dp(150)
                    allow_stretch: True
                MDBoxLayout:
                    orientation: 'vertical'
                    padding: dp(10)
                    spacing: dp(5)
                    MDLabel:
                        text: "Cost: 35000"
                        theme_text_color: 'Primary'
                        font_style: 'H6'
                        halign: 'center'
                    MDLabel:
                        text: "Location: Iyunga"
                        theme_text_color: 'Secondary'
                        font_style: 'Subtitle1'
                        halign: 'center'
                MDBoxLayout:
                    orientation: 'horizontal'
                    padding: dp(10)
                    spacing: dp(5)
                    pos_hint: {'center_x': .5}
                    MDFlatButton:
                        text: "Contacts"
                        theme_text_color: 'Primary'
                        font_style: 'H6'
                        pos_hint: {'center_x': .5}
                    MDIconButton:
                        icon: 'heart-outline'
                        theme_text_color: 'Custom'
                        text_color: 1, 0, 0, 1
                        user_font_size: '24sp'
    ''')
        self.grid.ids.grid.add_widget(card)
