from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty,StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
from kivy.uix.textinput import TextInput
import cv2
import numpy as np
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import sqlite3



class LiteEx(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        conn = sqlite3.connect('first_db.db')

        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS A(c TEXT,b TEXT)""")
        c.execute("DROP TABLE Customers;")

        conn.commit()

        conn.close()

    def submit(self):
        conn = sqlite3.connect('first_db.db')

        c = conn.cursor()

       
        c.execute("""INSERT INTO A(c, b) VALUES (?,?)""",
            (self.ids.word_input.text, self.ids.word_input.text)
        )


        #     'first': self.ids.word_input.text,
        #     'last' : self.ids.words_input.text,
        # })

        #     c.execute("""INSERT INTO Customers((firstname,lastname) VALUES (,)"""), {
        # 'first': self.ids.word_input.text,
        # 'last': self.ids.words_input.text,
        # })

        self.ids.word_label.text = f'{self.ids.word_input.text} Added'

        self.ids.word_input.text = ''

        conn.commit()

        conn.close()
        pass

    def show_name(self):

        conn = sqlite3.connect('first_db.db')

        c = conn.cursor()

        c.execute("SELECT * FROM A")
        records = c.fetchall()

        word = ''
        for record in records:
            word = f'{word}\n{record}'
            self.ids.word_label.text = f'{word}'


        conn.commit()

        conn.close()
        pass






class Container(Screen):
    text_input = ObjectProperty()
    label_wid = ObjectProperty()

    def change_label_text(self):
        self.label_wid.text = self.text_input.text

    pass 


class Inspection_page(Screen):
    checks = []

    def checkbox_click(self, instance, value, cage_no):
            # print(instance)
        # print(value)
        if value == True:
            Inspection_page.checks.append(cage_no)
            cage_selected = ", ".join(Inspection_page.checks)
            print(cage_selected)
            # self.ids.output_label.text = f"You selected: {cage_selected}"
        else:
            Inspection_page.checks.remove(cage_no)
            cage_selected = ", ".join(Inspection_page.checks)
            # self.ids.output_label.text = f"You selected: {cage_selected}"

    pass 


class NewScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.recv_2, 1.0/30.0)

    capture = cv2.VideoCapture('climbing_clip.mp4')



    # def recv_2(self, *args):
    #     cap = cv2.VideoCapture('climbing_clip.mp4')

    #     if not cap.isOpened():
    #         print("Error opening video")



    #     while(True):
    #         status, frame = cap.read()
    #         if status:
    #             buf = cv2.flip(frame, 0)
    #             image_texture = Texture.create(
    #                 size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #             image_texture.blit_buffer(
    #                 buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
    #             video = self.ids.image_source
    #             video.texture = image_texture

    #         else:
    #             break

   
                    # cv2.imshow('frame', frame)
            # key = cv2.waitKey(500)

            # if key == 32:
            #     cv2.waitKey()
            # elif key == ord('q'):
            #     break

    def recv(self, *args):
        ret, frame = self.capture.read()
        if ret:
            #flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video = self.ids.image_source
            video_1 = self.ids.image_source_1
            video_2 = self.ids.image_source_2
            video_3 = self.ids.image_source_3
            video.texture = image_texture
            video_1.texture = image_texture
            video_2.texture = image_texture
            video_3.texture = image_texture
        pass




class Piction(Screen):
    cont = StringProperty("0")

    # selected_btn_label = StringProperty()
    selected_btn_label = None
    popup = Popup(title='Animal IDs', size_hint=(None, None),size=(500,500),
         background="images/black.jpg")

    def display(self):
        pic_frame = self.manager.get_screen("container")
        print(pic_frame.ids.text_input.text)
        self.cont = pic_frame.ids.text_input.text

    def select_id(self):
        pop_layout = GridLayout(cols=1)
        # self.selected_btn_label = Label(text="")
        # pop_layout.add_widget(self.selected_btn_label)
        box = GridLayout(cols=1, spacing=4,padding=5,size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))

   
        for i in range(1, 37):
            if len(str(i)) == 1:
                btn1 = Button(text="98900102505680" + str(i),size_hint_x=0.2, size_hint_y=None,height=50)
            else:
                btn1 = Button(text="98900102505686" + str(i),size_hint_x=0.2, size_hint_y=None,height=50)

            # print(btn1.text)
            box.add_widget(btn1)
            # btn1.text = 
            btn1.bind(on_press=self.callback)
            btn1.bind(on_release=self.popup.dismiss)

        scroll = ScrollView(do_scroll_x=False,do_scroll_y=True, size_hint=(None, None),size=(400, 400))
        scroll.add_widget(box)
        pop_layout.add_widget(scroll)
        self.popup.content = pop_layout
        self.popup.open()

        # self.btn.bind(on_release=selpopup.dismiss)

    
    # class Screen1(Screen):
    #     layout = 

    def callback(self,instance):
        self.selected_btn_label = instance.text
        # def callback(self, instance):
        print(self.selected_btn_label)

    # def dismiss_pop(self):
    #     self.popup.dismiss


class AnotherScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)


             # Arranging Canvas
        with self.canvas:
 
            Color(255, 255, 255, 1)  # set the colour

            self.rect = Rectangle(pos = self.center,
                                  size_hint =(self.width,
                                        self.height))

            video_layout = GridLayout(rows=3)
            box_layout=BoxLayout(orientation='horizontal',size_hint=(1,None),height=44,pos_hint={"top":1})
            box_layout.add_widget(Label(text='   Date: '+ str(self.my_text), height=24,text_size=(box_layout.width,None)))
            box_layout.add_widget(Label(text='   Time: ' + str(self.my_text_2),height=24, text_size=(box_layout.width, None)))

            video_layout.add_widget(box_layout)
            video_layout.add_widget(Button(text='press 1'))
            video_layout.add_widget(Button(text='press 2'))

            # Setting the size and position of canvas

            # self.rect = Rectangle(pos = self.top,
            #                       size_hint =(self.width,
            #                             None),height=44.0)
 
            # # Update the canvas as the screen size change
            self.bind(pos = self.update_rect,
                  size = self.update_rect)
 
    # update function which makes the canvas adjustable.
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        # self.video_layout = GridLayout(rows=3)
        # self.video_layout.add_widget(Button(text='press 1'))
        # self.video_layout.add_widget(Button(text='press 2'))

       
        

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")
    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")
    

    # def video_layout(self,*args):
    # video_layout=GridLayout(rows=3)
    # box_layout=BoxLayout(orientation='horizontal',size_hint=(1,None),height=44,pos_hint={"top":1})
    # box_layout.add_widget(Label(text='   Date: '+ str(my_text), height=24,text_size=(box_layout.width,None)))
    # box_layout.add_widget(Label(text='   Time: ' + str(my_text_2),height=24, text_size=(box_layout.width, None)))

    # self.video_layout.add_widget(box_layout)
    # self.video_layout.add_widget(Button(text='press 1'))
    # self.video_layout.add_widget(Button(text='press 2'))

        # return video_layout

    

   



    pass 


# class KivyCamera(Image):
#     def __init__(self, capture, fps, **kwargs):
#         super(KivyCamera, self).__init__(**kwargs)
#         self.capture = capture
#         Clock.schedule_interval(self.update, 1.0 / fps)

#     def update(self, dt):
#         ret, frame = self.capture.read()
#         if ret:
#             # convert it to texture
#             buf1 = cv2.flip(frame, 0).tostring()
#             image_texture = Texture.create(
#                 size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             image_texture.blit_buffer(buf1, colorfmt='bgr', bufferfmt='ubyte')
#             # display image from the texture
#             self.texture = image_texture



# class VideoExample(Screen):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         Clock.schedule_interval(self.update_clock, 1)
        

#     my_text = StringProperty("0")
#     my_text_2 = StringProperty("0")
#     # datetime object containing current date and time
#     now = datetime.now()
#     my_text = now.strftime("%B %d, %Y")

#     def update_clock(self, *args):
#         # Called once a second using the kivy.clock module
#         # Add one second to the current time and display it on the label
#         self.now = self.now + timedelta(seconds=1)
#         self.my_text_2 = self.now.strftime("%H:%M:%S")


#     rtmp_add = " "

#     def setting_btn(self):
#         bigger_box = GridLayout(rows=2,spacing=10)
#         box = GridLayout(cols=2)
#         box.add_widget(Label(text="IpAddress: "))
#         self.st = TextInput(text="")
#         box.add_widget(self.st)
#         box.add_widget(Label(text="Port: "))
#         self.pt = TextInput(text="")
#         box.add_widget(self.pt)
#         self.rtmp_add = Label(text="rtmp:// " + self.st.text + ": " + self.pt.text + "/enclosure/live")
#         box.add_widget(self.rtmp_add)
#         bigger_box.add_widget(box)
#         set_box = GridLayout(cols=3, size_hint_y= None,
#                              height=50)
#         set_box.add_widget(Label(text=""))
#         btn = Button(text="Set", background_color=(0,1,0,1))
#         btn.bind(on_press=self.setProcess)
#         set_box.add_widget(btn)
#         set_box.add_widget(Label(text=""))
#         bigger_box.add_widget(set_box)
#         self.popup = Popup(title='Settings',content=bigger_box,size_hint=(.6,.4))
#         self.popup.open()
#         pass 

#     def setProcess(self, btn):
#         try:
#             self.ipAddress = self.st.text
#             self.port = self.pt.text
#             print("ip_address: ", self.ipAddress)
#             print("port: ", self.port)
#             print("address= ",self.rtmp_add.text)
#         except:
#             pass

#         self.popup.dismiss()

#     def back_btn(self):
#         self.manager.current="container"
#         pass 

#     capture = cv2.VideoCapture('myvid.mp4')

#     def playPause(self):
#         if self.ids.play_stop_btn.text == "Stop":
#             # self.ids.play_stop_btn.background_color = (0, 0, 1, 1)
#             self.stop()
            
#         else:
#             self.ids.play_stop_btn.text = "Stop"
#             self.ids.play_stop_btn.background_color = (1, 0, 0, 1)
#             Clock.schedule_interval(self.recv, 1.0/30.0)

    
#     def stop(self):
#         self.ids.play_stop_btn.text = "Play"
#         self.ids.play_stop_btn.background_color = (0,0,1,1)
#         cv2.waitKey(0)
#         # self.capture.release()
#         # self.ids.image_source.source = "images/foo.jpg"
#             # self.recv()

#     def recv(self, *args):
#         # myrtmp_addr = "rtmp://myip:1935/myapp/mystream"
#         # myrtmp_addr = "rtmp://myip:1935/myapp/mystream"
#         ret, frame = self.capture.read()
#         if ret:
#             #flip upside down
#             buf = cv2.flip(frame, 0)
#             image_texture = Texture.create(
#                 size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             image_texture.blit_buffer(
#                 buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
#             video = self.ids.image_source
#             video.texture = image_texture


#         # if self.ipAddress == None or self.port == None:
#         #     box = GridLayout(cols=1)
#         #     box.add_widget(Label(text="Ip or Port Not Set"))
#         #     btn = Button(text="OK")
#         #     btn.bind(on_press=self.closePopup)
#         #     box.add_widget(btn)
#         #     self.popup1 = Popup(title='Error',content=box,size_hint=(.8,.3))
#         #     self.popup1.open()
#         # else:
#         #     if self.ids.play_stop_btn.text == "Stop":
#         #         self.stop()
#         #     else:
#         #         self.ids.play_stop_btn.text = "Stop"
#         #         Clock.schedule_interval(self.recv, 0.1)

#     # def close(self,btn):
#     #     self.popup1.dismiss()

#     # def stop(self):
#     #     self.ids.play_stop_btn.text = "Play"
#     #     self.ids.play_stop_btn.background_color = (0,0,1,1)
#     #     self.capture.release()
#         # self.capture.destroyAllWindows()
#         # Clock.unschedule(self.recv)

    
#     #             # convert it to texture
#     #             buf1 = cv2.flip(frame, 0)
#     #             buf = buf1.tostring()
#     #             image_texture = Texture.create(
#     #                 size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#     #             image_texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
#     #             # display image from the texture
#     #             self.texture = image_texture

#             # width = int(self.capture.get(3))
#             # height = int(self.capture.get(4))

#             # image = np.zeros(frame.shape, np.uint8)

#             # smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

#             # image[:height//2, :width//2] = smaller_frame
#             # image[height//2:, :width//2] = smaller_frame
#             # image[:height//2, width//2:] = smaller_frame
#             # image[height//2:, width//2:] = smaller_frame

#             # cv2.imshow('frame', frame)

#         #     if cv2.waitKey(1) == ord('q'):
#         #         break

#         # cap.release()
#         # cap.destroyAllWindows()
#         # print(cv2.getBuildInformation())
#         # clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         # clientsocket.connect((self.ipAddress, self.port))
#         # received = []
#         # while True:
#         # 	recvd_data = clientsocket.recv(230400)
#         # 	if not recvd_data:
#         # 		break
#         # 	else:
#         # 		received.append(recvd_data)
#         # dataset = ''.join(received)
#         # image = pygame.image.fromstring(dataset,(640, 480),"RGB") # convert received image from string
#         # try:
#         # 	pygame.image.save(image, "foo.jpg")
#         # 	self.ids.image_source.reload()
#         # except:
#         # 	pass
#         pass


#     # def setting(self):
#     #     box = GridLayout(cols = 2)
#     #     box.add_widget(Label(text="IpAddress: ")
#     #     self.st = TextInput(id= "serverText")
#     #     box.add_widget(self.st)
#     #     box.add_widget(Label(text="Port: "))
#     #     self.pt = TextInput(id= "portText")
#     #     box.add_widget(self.pt)
#     #     btn = Button(text="Set", bold=True)
#     #     btn.bind(on_press=self.settingProcess)
#     #     box.add_widget(btn)
#     #     self.popup = Popup(title='Settings',content=box,size_hint=(.6,.4))
#     #     self.popup.open()

#     # def settingProcess(self, btn):
#     #     try:
#     #         self.ipAddress = self.st.text
#     #         self.port = int(self.pt.text)
#     #     except:
#     #         pass

#     #     self.popup.dismiss()
 





class WindowManagerEx(ScreenManager):
    pass

class MyApp(App):
    def build(self):
        self.sm = WindowManagerEx()
        return self.sm
    #     layout = BoxLayout(orientation='vertical')
    #     self.image = Image()
    #     layout.add_widget(self.image)
    #     layout.add_widget(Button(text='Click here',pos_hint={'center_x': .5,'center_y':.5},size_hint=(None,None)))
        
    #     Clock.schedule_interval(self.load_video,1.0/30.0)
    #     return layout

    
    # def load_video(self,*args):
    #     self.capture = cv2.VideoCapture("myvid.mp4")
    #     ret, frame = self.capture.read()

    #     self.image_frame = frame
    #     buffer = cv2.flip(frame,0).tostring()
    #     image_texture_1 = Texture.create(
    #         size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
    #     image_texture_1.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
    #     self.texture = image_texture_1


    # def build(self):
    #     grid = SelectableGrid(cols=3, rows=2, touch_multiselect=True,
    #                           multiselect=True)
    #     for i in range(0, 6):
    #         grid.add_widget(Button(text="Button {0}".format(i)))
    #     return grid




     
    pass 

    # def build(self):
    #     return WindowManager()


if __name__ == '__main__':
    MyApp().run()
