from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.clock import Clock
import socket


ESP32_IP = "192.168.43.114"  # Replace with the ESP32's IP address

class IoTApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.data_label = Label(text="Waiting for data...")
        self.button_on = Button(text="LED ON")
        self.button_off = Button(text="LED OFF")

        self.button_on.bind(on_press=self.send_high)
        self.button_off.bind(on_press=self.send_low)

        layout.add_widget(self.data_label)
        layout.add_widget(self.button_on)
        layout.add_widget(self.button_off)

        # Schedule the update function to run every second
        Clock.schedule_interval(self.update_data, 1)

        return layout

    def send_high(self, instance):
        UrlRequest("http://" + ESP32_IP + "/HIGH", on_success=self.handle_response)

    def send_low(self, instance):
        UrlRequest("http://" + ESP32_IP + "/LOW", on_success=self.handle_response)

    def handle_response(self, request, response):
        print(response)

    def update_data(self, dt):
        # Request sensor data from ESP32
        UrlRequest("http://" + ESP32_IP + "/data", on_success=self.handle_data)

    def handle_data(self, request, response):
        self.data_label.text = "Distance: " + response + " cm"

if __name__ == "__main__":
    
    IoTApp().run()