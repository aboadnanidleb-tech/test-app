from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='مرحبا! هذا أول تطبيق لي\nاشتغل بنجاح 🎉', 
                     font_size=30, 
                     halign='center')

MyApp().run()
