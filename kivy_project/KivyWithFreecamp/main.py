from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.popup import Popup
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.actionbar import ActionBar
 
class WelcomePage(Screen):
    pass

class ByePage(Screen):
    pass

class FirstPage(Screen):
    pass

class FirstWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class ThirdWindow(Screen):
    pass

class FourthWindow(Screen):
    pass

class FifthWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass 

class WidgetsExample(GridLayout):
    my_text = StringProperty("0")
    slider_value_txt = StringProperty("Value")
    count = 0
    count_enabled = BooleanProperty(False)
    text_input_str = StringProperty("foo")

    def on_click_left_button(self):
        print("left button clicked")
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
        
    def on_click_right_button(self):
        print("right button clicked")
        self.my_text = "Great"
    
    def on_toggle_button_state(self,widget):
        print("toggle state:" + widget.state)
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True
    
    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    # def on_slider_value(self, widget):
    #     # print("Slider: " + str(int(widget.value)))
    #     # self.slider_value_txt = str(int(widget.value))

    def on_text_validate(self, widget):
        self.text_input_str = widget.text

    def btn(self):
        show_popup()


class PopupExample(FloatLayout):
    pass

def show_popup():
    show = PopupExample()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None), size=(400,400))

    popupWindow.open()
            

class BoxLayoutExample(BoxLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text='A')
    #     b2 = Button(text='B')
    #     b3 = Button(text='C')
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)
    pass

class GridLayoutWork(GridLayout):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     # self.orientation="rl-tb"
       
    #     for i in range(0, 12):
    #         size = dp(100)
    #         # b = Button(text=str(i + 1), size_hint=(0.2, 0.2))
    #         b = Button(text=str(i + 1))
    #         self.add_widget(b)
    pass 
    
    # def on_press_button(self):
        

class AnchorLayoutExample(AnchorLayout):
    pass

class ActionBarExample(ActionBar):
    pass

# class GridLayoutExample(GridLayout):
#     pass


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation="rl-tb"
       
        for i in range(0, 100):
            size = dp(100)
            # b = Button(text=str(i + 1), size_hint=(0.2, 0.2))
            b = Button(text=str(i + 1), size_hint=(None, None), size = (size,size))
            self.add_widget(b)


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=2)
            Color(0, 1, 1)
            Line(circle=(400, 200, 50), width=2)
            Color(1, 0, 1)
            Line(rectangle=(600, 200, 100,70), width=2)
            Color(1, 1, 0)
            Line(ellipse=(500, 200, 80, 60), width=2)
            self.rect = Rectangle(pos=(100, 300), size=(100, 70))

    def on_click_button_a(self):
        # print("working")
        x, y = self.rect.pos
        w, h = self.rect.size
        inc = dp(10)
        diff = self.width - (x + w)
        if diff < inc:
            inc = diff
        x += inc
        self.rect.pos =(x,y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))
            
        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print("on size: " + str(self.width) + ", " + str(self.height))
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)
    
    def update(self, dt):
        # print("update")
        x, y = self.ball.pos
        x += self.vx
        y += self.vy

        if y + self.ball_size > self.height:
            y = self.height-self.ball_size
            self.vy = -self.vy
        if x + self.ball_size > self.width:
            x = self.width-self.ball_size
            self.vx = -self.vx
        if y < 0:
            y = 0
            self.vy = -self.vy
        if x < 0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x,y)

class CanvasExample6(Widget):
    pass

class CanvasExample7(Widget):
    pass

if __name__ == "__main__":
    TheLabApp().run()
