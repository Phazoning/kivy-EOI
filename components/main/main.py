from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.slider import Slider


class Main(FloatLayout):

    def __init__(self, **kwargs):

        FloatLayout.__init__(self, **kwargs)
        self.mainText = TextInput(text="Text to de/code")
        self.resultText = Label(text="Output text")
        self.funButton = Button(text="De/code")
        self.exButton = Button(text="Exchange")
        self.randVar = Button(text="Set a random key")
        self.key = Slider(text="Choose a key")

        self.add_widget(self.mainText)
        self.add_widget(self.resultText)
        self.add_widget(self.funButton)
        self.add_widget(self.exButton)
        self.add_widget(self.randVar)
        self.add_widget(self.key)
