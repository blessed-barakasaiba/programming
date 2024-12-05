import kivy
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import serial

kivy.require('2.1.0')  # Replace with your Kivy version

class ArduinoApp(MDApp):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label to display Arduino status
        self.status_label = MDLabel(
            text="Waiting for data...",
            halign="center",
            theme_text_color="Secondary"
        )
        self.layout.add_widget(self.status_label)

        # Connect to Arduino serial port
        self.ser = serial.Serial('COM33', 115200)  # Update COM port based on your system

        # Schedule a method to read serial data periodically
        Clock.schedule_interval(self.read_arduino_data, 1)

        return self.layout

    def read_arduino_data(self, dt):
        # Read data from the serial port
        if self.ser.in_waiting > 0:
            data = self.ser.readline().decode('utf-8').strip()  # Read a line of data
            print(f"Arduino Data: {data}")  # Debugging purpose

            # Update the label based on data
            if "Motion Detected" in data:
                self.status_label.text = "Motion Detected: Light ON"
            elif "No Motion" in data:
                self.status_label.text = "No Motion: Light OFF"

    def on_stop(self):
        # Close the serial connection when the app stops
        if self.ser.is_open:
            self.ser.close()

if __name__ == "__main__":
    ArduinoApp().run()
