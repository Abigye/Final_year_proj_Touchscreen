from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class GameScreen(Widget):
    pass


class SecondKivyApp(App):
    def build(self):
        return GameScreen()


if __name__== '__main__':
   SecondKivyApp().run()