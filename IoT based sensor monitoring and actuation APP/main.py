from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.network.urlrequest import UrlRequest
from kivy.properties import StringProperty

class ESP32ControlLayout(BoxLayout):
    esp32_data = StringProperty()
    
    def __init__(self, **kwargs):
        super(ESP32ControlLayout, self).__init__(**kwargs)
        self.update_esp32_data()
    
    def update_esp32_data(self, *args):
        url = "http://<esp32_ip_address>/data"
        UrlRequest(url, on_success=self.handle_response, on_error=self.handle_error)
    
    def handle_response(self, request, response):
        self.esp32_data = response
    
    def handle_error(self, request, error):
        print("Error:", error)
    
    def send_control_signal(self, control_signal):
        url = "http://<esp32_ip_address>/control?signal={}".format(control_signal)
        UrlRequest(url, on_success=self.handle_response, on_error=self.handle_error)

class ESP32ControlApp(App):
    def build(self):
        return ESP32ControlLayout()

if __name__ == '__main__':
    ESP32ControlApp().run()