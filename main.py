from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        self.label = Label(text='مرحبا! هذا أول تطبيق لي', font_size=24)
        layout.add_widget(self.label)
        
        self.text_input = TextInput(hint_text='اكتب أي شيء هنا', multiline=False, font_size=20)
        layout.add_widget(self.text_input)
        
        button = Button(text='اضغط هنا', font_size=20, size_hint_y=0.3)
        button.bind(on_pressآسف والله، صار عندي لقطة وطلعلك رسالة غلط بالإنجليزي 😅

رجاع للموضوع:

الكود يلي بعته:
```python
print("مرحبا! هذا أول تطبيق لي")
print("اكتب أي شيء واضغط Enter")
while True:
    x = input(">>> ")
    print("أنت كتبت:", x)
