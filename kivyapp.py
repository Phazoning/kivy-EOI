import kivy
from components.main.main import Main

kivy.require('2.0.0')

from kivy.app import App

class KivyApp(App):

    def build(self):
        return Main()

if __name__ == '__main__':
    KivyApp.build()