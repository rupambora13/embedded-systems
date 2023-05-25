from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import socket


class Esp32App(App):
    def build(self):
        # Create UI
        layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text='Disconnected')
        self.connect_button = Button(text='Connect')
        self.disconnect_button = Button(text='Disconnect', disabled=True)

        layout.add_widget(self.status_label)
        layout.add_widget(self.connect_button)
        layout.add_widget(self.disconnect_button)

        self.connect_button.bind(on_press=self.connect)
        self.disconnect_button.bind(on_press=self.disconnect)

        return layout

    def connect(self, instance):
        try:
            # Create socket connection to ESP32 server
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect(('192.168.43.114', 80))  # Replace 'ESP32_IP_ADDRESS' with the actual IP address of your ESP32
            self.status_label.text = 'Connected'
            self.connect_button.disabled = True
            self.disconnect_button.disabled = False
        except Exception as e:
            self.status_label.text = f'Error: {e}'

    def disconnect(self, instance):
        try:
            # Close socket connection to ESP32 server
            self.sock.close()
            self.status_label.text = 'Disconnected'
            self.connect_button.disabled = False
            self.disconnect_button.disabled = True
        except Exception as e:
            self.status_label.text = f'Error: {e}'

    def on_stop(self):
        try:
            # Close socket connection when the app is closed
            self.sock.close()
        except:
            pass


if __name__ == '__main__':
    Esp32App().run()