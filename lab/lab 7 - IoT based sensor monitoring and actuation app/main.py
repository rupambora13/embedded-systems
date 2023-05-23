from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Line


class IoT(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Add a label widget
        label = Label(text='Hello Kivy!',
                      font_size='50sp',
                      size_hint=(1, 1))
        layout.add_widget(label)

        # Add a border to the layout
        with layout.canvas:
            Color(1, 0, 0, 1)  # Set border color (red)
            Line(rectangle=(0, 0, 360, 640),
                 width=2)

        return layout


if __name__ == '__main__':
    Config.set('graphics', 'width', '360')
    Config.set('graphics', 'height', '640')
    Config.set('graphics', 'orientation', 'portrait')

    IoT().run()