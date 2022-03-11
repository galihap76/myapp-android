from kivy.app import App
from kivy.uix.button import Button
 
class Myapp(App):
    def build(self):
        def app(instance,value):
            pass
        btn = Button(text="I am a programmer!",font_size=50)
        btn.bind(state=app)
        return btn
 
 
if __name__ == "__main__":
    Myapp().run()
