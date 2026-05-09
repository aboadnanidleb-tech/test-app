from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text='المبرمج عبد العزيز\nأول تطبيق لي اشتغل بنجاح 🎉', 
                     font_size=30, 
                     halign='center',
                     valign='middle')

MyApp().run()
