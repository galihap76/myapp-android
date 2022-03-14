from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.pagelayout import PageLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class Myapp(App):
    def build(self):
        Window.clearcolor = ('white')
        layout = FloatLayout()
        btn = Button(text='CLICK', font_size=20, size=(70, 50), size_hint=(None, None),
                     pos=(650, 350),
                     background_color=('black'))
        return btn
        return layout 

if __name__ == "__main__":
    Myapp().run()
