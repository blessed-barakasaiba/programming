from kivymd.uix.button import MDButton

class ArduinoApp(App):
    def build(self):
        button = MDButton()
        button.text = "Click me"
        return button
