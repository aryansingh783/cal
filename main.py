from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        self.display = TextInput(
            font_size=32,
            readonly=True,
            halign="right",
            size_hint=(1, 0.2)
        )
        self.add_widget(self.display)

        buttons = [
            ["7","8","9","/"],
            ["4","5","6","*"],
            ["1","2","3","-"],
            ["0","C","=","+"]
        ]

        for row in buttons:
            row_layout = BoxLayout()
            for label in row:
                btn = Button(text=label, font_size=24)
                btn.bind(on_press=self.on_button_press)
                row_layout.add_widget(btn)
            self.add_widget(row_layout)

    def on_button_press(self, instance):
        text = instance.text
        if text == "C":
            self.display.text = ""
        elif text == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Error"
        else:
            self.display.text += text

class CalcApp(App):
    def build(self):
        return Calculator()

CalcApp().run()