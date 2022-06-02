from kivy.app import App
from kivy.uix.button import Button 


class FunkyButton(Button):

    # def __init__(self, **kwargs):
    #     super(FunkyButton, self).__init__(**kwargs)
    #     self.text='Hi Funky Button!'
    #     self.pos=(100,100)
    #         # size=(100, 100),
    #     self.size_hint=(0.25,0.25)
        pass


class FirstKivyApp(App):
    def build(self):
        return FunkyButton(
            pos=(50,50),
            size_hint=(None, None) ,
            size=(500,500)
        )

    # def build(self):
    #     return Button(
    #         text='Hello World',
    #         pos=(50,50),
    #         # size=(100, 100),
    #         size_hint=(0.8,0.8))


if __name__== '__old_main__':
    FirstKivyApp().run()