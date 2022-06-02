# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.widget import Widget
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.anchorlayout import AnchorLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.stacklayout import StackLayout
# from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.scrollview import ScrollView
# from kivy.metrics import dp
# from kivy.uix.screenmanager import ScreenManager, Screen 
# from kivy.uix.pagelayout import PageLayout
# from kivy.properties import StringProperty, BooleanProperty, Clock
# from kivy.uix.popup import Popup
# from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
# from kivy.graphics.context_instructions import Color
# from kivy.uix.actionbar import ActionBar

# from kivy.core.window import Window
# Window.keyboard_anim_args = {'d': .2, 't': 'in_out_expo'}
# Window.softinput_mode = "below_target"
 
# class WelcomePage(Screen):
#     pass

# class ByePage(Screen):
#     pass

# class FirstPage(Screen):
#     pass

# class FirstWindow(Screen):
#     pass

# class SecondWindow(Screen):
#     pass

# class WindowManager(ScreenManager):
#     pass

# class Pager(Widget):
#     pass 
        

# class TheTouchScreenRecorder(App):
#     pass

# class ThirdWindow(Screen):
#     pass 
# class CanvasExample5(Widget):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.ball_size = dp(50)
#         self.vx = dp(3)
#         self.vy = dp(4)
#         with self.canvas:
#             self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            
#         Clock.schedule_interval(self.update, 1/60)

#     def on_size(self, *args):
#         # print("on size: " + str(self.width) + ", " + str(self.height))
#         self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)
    
#     def update(self, dt):
#         # print("update")
#         x, y = self.ball.pos
#         x += self.vx
#         y += self.vy

#         if y + self.ball_size > self.height:
#             y = self.height-self.ball_size
#             self.vy = -self.vy
#         if x + self.ball_size > self.width:
#             x = self.width-self.ball_size
#             self.vx = -self.vx
#         if y < 0:
#             y = 0
#             self.vy = -self.vy
#         if x < 0:
#             x = 0
#             self.vx = -self.vx

#         self.ball.pos = (x,y)

# if __name__ == "__main__":
#     TheTouchScreenRecorder().run()
