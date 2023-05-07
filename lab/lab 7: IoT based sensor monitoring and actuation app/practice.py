import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config

Config.set('graphics','resizable', True)

class MyApp(App):
    def build(self):
        F1 = FloatLayout()
        btn = Button(text = 'Hello World', size_hint = (.3,.2), pos = (300,200))
        F1.add_widget(btn)
        return F1

MyApp().run()

