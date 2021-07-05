from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.properties import StringProperty, BoundedNumericProperty
from functions.functions import Functions as Fun
from random import randint


class Main(GridLayout):

    def __init__(self, **kwargs):

        GridLayout.__init__(self, **kwargs)
        self.mainText = TextInput(text="") #The text to be codified or decodified
        self.resultText = Label(text="") #De/codified text
        self.funButtonText = StringProperty("De/code") #Text of the button which applies the de/codifying method
        self.exButtonText = StringProperty("Exchange") #Text of the button which exchanges texts
        self.randVarButtonText = StringProperty("Set a random key") #Text of the button which sets a random key
        self.keyCont = BoundedNumericProperty(0, min=-26, max=26) #Value of the key, bounded on Z_27

    def exchange_texts(self):
        """
        This method exchanges the processed and original texts
        """
        main = self.mainText.text
        result = self.resultText
        self.mainText = result
        self.resultText = main

    def process_text(self):
        """
        This method retrieves the data and processes the text
        """
        self.resultText.text = Fun.cifra(self.mainText.text, self.keyCont)

    def random_key(self):
        """
        This method sets the key on a random integer
        """
        self.keyCont = randint(-26, 27)

    def show_slider(self, widget):
        """
        This method sets the value of the key
        :param widget:
        """
        self.keyCont = int(widget.value)