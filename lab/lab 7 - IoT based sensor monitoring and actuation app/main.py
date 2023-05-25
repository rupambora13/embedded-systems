from kivy.config import Config
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.clock import Clock
import socket

class IoT(App):
    def build(self):
        # Create UI
        layout = BoxLayout(orientation='vertical')

        self.data_label = Label(text='Waiting for data...')
        self.button_on = Button(text='LED ON')
        self.button_off = Button(text='LED OFF')

        layout.add_widget(self.data_label)
        layout.add_widget(self.button_on)
        layout.add_widget(self.button_off)
       
        # Open socket connection to ESP32 server
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect(('192.168.43.114', 80))  # Replace 'ESP32_IP_ADDRESS' with the IP address of your ESP32
        

        self.button_on.bind(on_press=self.send_high)
        self.button_off.bind(on_press=self.send_low)
        
        # Schedule the update function to run every second
        Clock.schedule_interval(self.update_data, 1)
        
        return layout
    
    def update_data(self, dt):
        # Receive data from the ESP32 server
        data = self.sock.recv(1024).decode().strip()
        
        # Update the UI label with the received data
        self.data_label.text = data

    def send_high(self, instance):
        # Send "HIGH" command to the ESP32 server
        self.sock.sendall(b"HIGH\n")
    
    def send_low(self, instance):
        # Send "LOW" command to the ESP32 server
        self.sock.sendall(b"LOW\n")

    def on_stop(self):
        # Close the socket connection when the app is closed
        self.sock.close()
    

if __name__ == '__main__':
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')
    Config.set('graphics', 'orientation', 'portrait')
    
    IoT().run()