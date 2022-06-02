from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, StringProperty
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from KivyCalendar import DatePicker
from kivy.uix.popup import Popup
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.vkeyboard import VKeyboard
from kivy.factory import Factory
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
from kivy.graphics.texture import Texture
from FileReadAndWriter import write_to_text_file
import cv2


# myrtmp_addr = "rtmp://myip:1935/myapp/mystream"
# cap = cv2.VideoCapture(myrtmp_addr)
# frame, err = cap.read()

# From there you can handle your frames like when you get it from your cam. 
# if it still doesn't work, check if you have a valid version of ffmpeg linked 
# with your opencv. 
# You can check it with print(cv2.getBuildInformation())

class VideoEx(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        

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


    def setting_btn(self):
        bigger_box = GridLayout(rows=2,spacing=10)
        box = GridLayout(cols=2)
        box.add_widget(Label(text="IpAddress: "))
        self.st = TextInput(text="")
        box.add_widget(self.st)
        box.add_widget(Label(text="Port: "))
        self.pt = TextInput(text="")
        box.add_widget(self.pt)
        bigger_box.add_widget(box)
        set_box = GridLayout(cols=3, size_hint_y= None,
                                height=50)
        set_box.add_widget(Label(text=""))
        btn = Button(text="Set", background_color=(0,1,0,1))
        btn.bind(on_press=self.setProcess)
        set_box.add_widget(btn)
        set_box.add_widget(Label(text=""))
        bigger_box.add_widget(set_box)
        self.popup = Popup(title='Settings',content=bigger_box,size_hint=(.6,.4))
        self.popup.open()
        pass 

    def setProcess(self, btn):
        try:
            self.ipAddress = self.st.text
            self.port = self.pt.text
            print("ip_address: ", self.ipAddress)
            print("port: ", self.port)
        except:
            pass

        self.popup.dismiss()

    def back_btn(self):
        self.manager.current="container"
        pass 


    capture = cv2.VideoCapture('myvid.mp4')


    def playPause(self):
        if self.ids.play_stop_btn.text == "Stop":
            # self.ids.play_stop_btn.background_color = (0, 0, 1, 1)
            self.ids.play_stop_btn.background_color = (0, 0, 1, 1)
            self.ids.play_stop_btn.text = 'Play'
            self.capture.release()
            self.ids.image_source.reload()
            # cv2.waitKey(0)
          
            

        else:
            Clock.schedule_interval(self.recv, 1.0/30.0)
            self.ids.play_stop_btn.text = "Stop"
            self.ids.play_stop_btn.background_color = (1, 0, 0, 1)




    # def stop(self):

    #     if self.ids.play_stop_btn.text == "Play":
    #         self.playPause()

    #     else:
    #         self.ids.play_stop_btn.text = "Play"
    #         self.ids.play_stop_btn.background_color = (0, 0, 1, 1)
    #         # cv2.waitKey(1)
    #         self.capture.release()
    #         self.ids.image_source.reload()

        
    def recv(self, *args):
        # myrtmp_addr = "rtmp://myip:1935/myapp/mystream"
        ret, frame = self.capture.read()
        if ret:
            #flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video = self.ids.image_source
            video.texture = image_texture


class Inspection(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        

    checks = []

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

    def checkbox_click(self, instance, value, cage_no):
        # print(instance)
        # print(value)
        if value == True:
            Inspection.checks.append(cage_no)
            cage_selected = ", ".join(Inspection.checks)
            self.ids.output_label.text = f"You selected: {cage_selected}"
        else:
            Inspection.checks.remove(cage_no)
            cage_selected = ", ".join(Inspection.checks)
            self.ids.output_label.text = f"You selected: {cage_selected}"
    
    def on_click_select_all(self):
        if  self.ids.select_all_btn.text == "Deselect All":
            self.ids.select_all_btn.text = "Select All"
            self.control_checkbox(False)
        elif self.ids.select_all_btn.text == "Select All":  
            self.ids.select_all_btn.text = "Deselect All"
            self.control_checkbox(True)
            self.confirmation_dialog_box()

    def control_checkbox(self,btn_state):
        self.ids.check_box_1.active=btn_state
        self.ids.check_box_2.active=btn_state
        self.ids.check_box_3.active=btn_state
        self.ids.check_box_4.active=btn_state
        self.ids.check_box_5.active=btn_state
        self.ids.check_box_6.active=btn_state
        self.ids.check_box_7.active=btn_state
        self.ids.check_box_8.active=btn_state
        self.ids.check_box_9.active=btn_state
        self.ids.check_box_10.active=btn_state
        self.ids.check_box_11.active=btn_state
        self.ids.check_box_12.active=btn_state

    confirm_dialog = Popup(
        title="Cage Inspection Confirmation",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    inputted_time = None
    end_time = None

    def confirmation_dialog_box(self):
        con_layout = GridLayout(rows=5, padding=10)
        con_layout.add_widget(Label(text="Confirm the cages have been inspected"))
        con_layout.add_widget(Label(text=""))

        sec_layout = GridLayout(cols=2)
        sec_layout.add_widget(Label(text="Inspection Start Time"))
        self.inputted_time = TextInput(text="", hint_text="9:16")
        sec_layout.add_widget(self.inputted_time)
        sec_layout.add_widget(Label(text="Inspection End Time"))
        self.end_time = TextInput(text="", hint_text="e.g 21:00")
        sec_layout.add_widget(self.end_time)

        con_layout.add_widget(sec_layout)
        con_layout.add_widget(Label(text=""))

        con_box = GridLayout(cols=3)
        con_layout.add_widget(con_box)
        YesButton = Button(text="Yes",background_color=(0, 1, 0, 1))
        con_box.add_widget(YesButton)
        NoButton = Button(text="No", background_color=(0, 0, 1, 1))
        con_box.add_widget(NoButton)
        CancelButton = Button(text="Cancel")
        con_box.add_widget(CancelButton)
        self.confirm_dialog.content = con_layout
        Clock.schedule_once(self.confirm_dialog.open, 1)

        YesButton.bind(on_press=self.confirm_dialog.dismiss)
        YesButton.bind(on_press=self.inspection_writing)
        YesButton.bind(on_release=self.change_screen_to_eventCat)
        YesButton.bind(on_release=self.deselect_selected_cages)
        
        NoButton.bind(on_press=self.confirm_dialog.dismiss)
    
        CancelButton.bind(on_press=self.confirm_dialog.dismiss)
        CancelButton.bind(on_release = self.change_screen_to_welcome)

    def deselect_selected_cages(self,YesButton):
        list_of_cage_ids = [self.ids.check_box_1,self.ids.check_box_2,self.ids.check_box_3,
        self.ids.check_box_4,self.ids.check_box_5,self.ids.check_box_6,self.ids.check_box_7,
        self.ids.check_box_8,self.ids.check_box_9,self.ids.check_box_10,self.ids.check_box_11,self.ids.check_box_12]
        
        for id in list_of_cage_ids:
            if id.active == True:
                id.active = False
    

    def inspection_writing(self,NoButton):
        cages_selected = self.ids.output_label.text.split(":")
        cages_to_write = ""
        if len(cages_selected)==1:
            cages_to_write = "No cages selected"
        else:
            cages_to_write = cages_selected[1]
        write_to_text_file(Event_category="Inspect Cages",Inspection_start_time=self.inputted_time.text,Inspection_end_time=self.end_time.text,Date=self.my_text,
        Time_recorded=self.my_text_2,Cages_Inspected=cages_to_write)


    def change_screen_to_eventCat(self,NoButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def change_screen_to_welcome(self,NoButton):
        self.manager.current='welcome'
        self.manager.transition.direction = 'left'


class WelcomePage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

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

    def get_time(self):
        self.time_on_next_button = datetime.now()
        self.time_on_next_button = self.time_on_next_button.strftime("%H:%M:%S")
        print(datetime.now())
        print(self.time_on_next_button)

    popup_time = Popup(title='How many minutes do you expect to spend in the lab', size_hint=(None, None),size=(400,400),
         background="images/purple.jpg")


    timespend = None

    popup = Popup(
        title="How much time do you expect to spend in the lab?",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    def onButtonPress(self):

        layout = GridLayout(rows=6, padding=10)
        unusedlabel = Label(text="")
        layout.add_widget(unusedlabel)

        popupLabel = Label(text="Enter number of minutes")
        layout.add_widget(popupLabel)
        self.input_text = TextInput(text="")
        layout.add_widget(self.input_text)
        unusedlabel3 = Label(text="")
        unusedlabel2 = Label(text="")
        layout.add_widget(unusedlabel2)
        layout.add_widget(unusedlabel3)
        box = GridLayout(cols=3)
        layout.add_widget(box)
        setButton = Button(text="Set", background_color=(0, 1, 0, 1))
        box.add_widget(setButton)
        skipButton = Button(text="Skip", background_color=(0, 0, 1, 1))
        box.add_widget(skipButton)
        cancelButton = Button(text="Cancel")
        box.add_widget(cancelButton)
        self.popup.content = layout
        self.popup.open()

        # Attach close button press with popup.dismiss action
        cancelButton.bind(on_press=self.popup.dismiss)

        skipButton.bind(on_press=self.popup.dismiss)
        skipButton.bind(on_release=self.change_screen_from_welcome_to_eventCat)

        setButton.bind(on_press=self.settingProcess)
        setButton.bind(on_release = self.change_screen_from_welcome_to_eventCat)

    def change_screen_from_welcome_to_eventCat(self,cancelButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def settingProcess(self, setButton):
        try:
            self.timespend = int(self.input_text.text)
            print(self.timespend)

            self.popup.dismiss()

        except:
            box_2 = GridLayout(rows=3)
            label_2 = Label(
                text="Number of minutes must be an integer \n between 0 and 60"
            )
            box_2.add_widget(label_2)
            label_1 = Label(text="")
            box_2.add_widget(label_1)
            button_2 = Button(text="Close")
            box_2.add_widget(button_2)
            popup_2 = Popup(
                title="Incorrect Number of Minutes",
                content=box_2,
                size_hint=(None, None),
                size=(300, 200),
                background="images/black.jpg",
            )

            popup_2.open()

            button_2.bind(on_press=popup_2.dismiss)

class GridWindow1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

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

    pass


class GridWindow2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")
    my_text_3 = StringProperty("ok")
    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    pass


class IndividualAnimalWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")
    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    cage_number = ObjectProperty(None)
    animal_id = ObjectProperty(None)
    event_category = ObjectProperty(None)
    duration = ObjectProperty(None)
    date = ObjectProperty(None)
    weight = ObjectProperty(None)
    dosage = ObjectProperty(None)
    description = ObjectProperty(None)
    anim_type = ObjectProperty(None)
    length = ObjectProperty(None)


    popup = Popup(title='Animal IDs', size_hint=(None, None),size=(400,300),
         background="images/black.jpg")

    def get_all_animal_ids(self):
        all_animal_ids = ["98900102505680" + str(i) if len(str(i)) == 1 else "9890010250568" + str(i) for i in range(1, 37)]
        return all_animal_ids



    def get_animal_ids_for_cage(self,value):
        num = int(value)
        if num == 1:
            animal_ids_for_selected_cage = self.get_all_animal_ids()[0:4]
        else:
            animal_ids_for_selected_cage = self.get_all_animal_ids()[
                ((num-1)*3)-1:num*3]

        return animal_ids_for_selected_cage
        
    def select_id(self):
        pop_layout = GridLayout(cols=1)
        box = GridLayout(cols=1, spacing=4,padding=5,size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
  
        for i in self.get_animal_ids_for_cage(self.cage_number.text):
            btn1 = Button(text=i,size_hint_x=0.2, size_hint_y=None,height=50)

            box.add_widget(btn1)
            btn1.bind(on_press=self.callback)
            btn1.bind(on_release=self.popup.dismiss)
        
        scroll = ScrollView(do_scroll_x=False,do_scroll_y=True, size_hint=(None, None),size=(300, 200))
        scroll.add_widget(box)
        pop_layout.add_widget(scroll)
        self.popup.content = pop_layout
        self.popup.open()

    def callback(self,instance):
        self.animal_id.text = instance.text
      
    # spinner drop down for type of event
    def spinner_clicked(self, value):
        self.ids.anim_type.text = value
        pass

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")


    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    def onPressFinish(self):
    
        layout = GridLayout(rows=6, padding=10)
        unusedlabel = Label(text="")
        layout.add_widget(unusedlabel)

        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        input_text = Label(text="")
        layout.add_widget(input_text)
        unusedlabel3 = Label(text="")
        unusedlabel2 = Label(text="")
        layout.add_widget(unusedlabel2)
        layout.add_widget(unusedlabel3)
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        SaveNewButton = Button(text="Save & New", background_color=(1, 0, 1, 1))
        box.add_widget(SaveNewButton)
        SaveExitButton = Button(text="Save & Exit", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)

        SaveNewButton.bind(on_press=self.press)
        SaveNewButton.bind(on_press=self.popup_finish.dismiss)
        SaveNewButton.bind(on_release=self.change_screen_to_eventCat)

        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release = self.change_screen_to_welcome)

    def press(self,EditButton):
        write_to_text_file(Cage_number=self.cage_number.text,Animal_ID=self.animal_id.text,Event_category=self.event_category.text,Duration=self.duration.text,Date=self.date.text,
        Weight=self.weight.text,Length=self.length.text, Dosage=self.dosage.text,Description=self.description.text,Type=self.anim_type.text)

        # self.popup_finish.dismiss()

    def change_screen_to_eventCat(self,EditButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def change_screen_to_welcome(self,EditButton):
        self.manager.current='welcome'
        self.manager.transition.direction = 'left'

class CageWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        # show = Pagge()

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")

    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    cage_number = ObjectProperty(None)
    event_category = ObjectProperty(None)
    duration = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    cage_type = ObjectProperty(None)


    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    def onPressFinish(self):
    
        layout = GridLayout(rows=6, padding=10)
        unusedlabel = Label(text="")
        layout.add_widget(unusedlabel)

        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        input_text = Label(text="")
        layout.add_widget(input_text)
        unusedlabel3 = Label(text="")
        unusedlabel2 = Label(text="")
        layout.add_widget(unusedlabel2)
        layout.add_widget(unusedlabel3)
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        SaveNewButton = Button(text="Save & New", background_color=(1, 0, 1, 1))
        box.add_widget(SaveNewButton)
        SaveExitButton = Button(text="Save & Exit", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)

        SaveNewButton.bind(on_press=self.press)
        SaveNewButton.bind(on_press=self.popup_finish.dismiss)
        SaveNewButton.bind(on_release=self.change_screen_to_eventCat)

        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release = self.change_screen_to_welcome)

    def press(self,EditButton):
        write_to_text_file(Cage_number=self.cage_number.text,Event_category=self.event_category.text,Duration=self.duration.text,Date=self.date.text,
        Description=self.description.text,Type=self.cage_type.text)

    def change_screen_to_eventCat(self,EditButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def change_screen_to_welcome(self,EditButton):
        self.manager.current='welcome'
        self.manager.transition.direction = 'left'

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def spinner_clicked(self, value):
        self.ids.cage_type.text = value

class RoomLevelWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")
    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    event_category = ObjectProperty(None)
    duration = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    room_type = ObjectProperty(None)


    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    def onPressFinish(self):
    
        layout = GridLayout(rows=6, padding=10)
        unusedlabel = Label(text="")
        layout.add_widget(unusedlabel)

        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        input_text = Label(text="")
        layout.add_widget(input_text)
        unusedlabel3 = Label(text="")
        unusedlabel2 = Label(text="")
        layout.add_widget(unusedlabel2)
        layout.add_widget(unusedlabel3)
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        SaveNewButton = Button(text="Save & New", background_color=(1, 0, 1, 1))
        box.add_widget(SaveNewButton)
        SaveExitButton = Button(text="Save & Exit", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)

        SaveNewButton.bind(on_press=self.press)
        SaveNewButton.bind(on_press=self.popup_finish.dismiss)
        SaveNewButton.bind(on_release=self.change_screen_to_eventCat)

        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release = self.change_screen_to_welcome)

    def press(self,EditButton):
        write_to_text_file(Event_category=self.event_category.text,Duration=self.duration.text,Date=self.date.text,
        Description=self.description.text,Type=self.room_type.text)

    def change_screen_to_eventCat(self,EditButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def change_screen_to_welcome(self,EditButton):
        self.manager.current='welcome'
        self.manager.transition.direction = 'left'

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def spinner_clicked(self, value):
        self.ids.room_type.text = value
        pass

 
class AddEventWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")

    now = datetime.now()
    # datetime object containing current date and time
    time_text = my_text_2
    my_text = now.strftime("%B %d, %Y")

    event_category = ObjectProperty(None)
    description = ObjectProperty(None)
    event_name = ObjectProperty(None)
    # event_type = ObjectProperty(None)
  
    def spinner_clicked(self, value):
        self.ids.event_category.text = value
        self.get_values_for_event_category(value)
        pass

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(400, 400),
        background="images/black.jpg",
    )

    def onPressFinish(self):
    
        layout = GridLayout(rows=6, padding=10)
        unusedlabel = Label(text="")
        layout.add_widget(unusedlabel)

        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        input_text = Label(text="")
        layout.add_widget(input_text)
        unusedlabel3 = Label(text="")
        unusedlabel2 = Label(text="")
        layout.add_widget(unusedlabel2)
        layout.add_widget(unusedlabel3)
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        SaveNewButton = Button(text="Save & New", background_color=(1, 0, 1, 1))
        box.add_widget(SaveNewButton)
        SaveExitButton = Button(text="Save & Exit", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)

        SaveNewButton.bind(on_press=self.add_to_event_cat)
        SaveNewButton.bind(on_press=self.popup_finish.dismiss)
        SaveNewButton.bind(on_release=self.change_screen_to_eventCat)

        SaveExitButton.bind(on_press=self.add_to_event_cat)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release = self.change_screen_to_welcome)

    def add_to_event_cat(self,EditButton):
        # print(self.event_category.text)
        screen_to_update = None
        if self.event_category.text == 'Individual Animal' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen("animal").anim_type.values.append(self.event_name.text)
        elif self.event_category.text == 'Cage' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen("cage").cage_type.values.append(self.event_name.text)
        elif self.event_category.text == 'Room Level' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen("room").room_type.values.append(self.event_name.text)

    def change_screen_to_eventCat(self,EditButton):
        self.manager.current='eventgrid'
        self.manager.transition.direction = 'left'

    def change_screen_to_welcome(self,EditButton):
        self.manager.current='welcome'
        self.manager.transition.direction = 'left'

    
    # event_category = ObjectProperty()

    def get_values_for_event_category(self,value):
        self.ids.event_type_label.text = 'Event type present for ' 
        if value == 'Individual Animal':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(self.manager.get_screen("animal").anim_type.values)
        elif value == 'Cage':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(
                self.manager.get_screen("cage").cage_type.values)
        elif value == 'Room Level':
           self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(
                self.manager.get_screen("room").room_type.values)
        
        print("cat= " + self.ids.event_type_label.text)
        # return event_type

   



    

    



class EventCategoryWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")


    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")


    category_value = None

    # def get_event_category(self,value):
    #     category_value = value
    #     print(category_value)
    #     # print(self.manager)
    #     return category_value 
        
    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")
    
    



class WindowManager(ScreenManager):
    my_global = StringProperty("")
    cage_ids = StringProperty("")



    pass


class TouchScreen(App):
    title = "Record"

    def build(self):
        self.sm = WindowManager()
        return self.sm


if __name__ == "__main__":
    TouchScreen().run()



  # i=5

    # min_label = None


    # def select_number_of_minutes(self):
    #     min_layout = GridLayout(cols=1)
    #     min_box = GridLayout(cols=2, spacing=28,size_hint_y=None)
    #     min_box.bind(minimum_height=min_box.setter('height'))

    #     min_box.add_widget(Label(text =''))
    #     min_box.add_widget(Label(text =''))


    #     check_label_5 = Label(text = "5  mins")
    #     min_box.add_widget(check_label_5)
    #     check_box_5= CheckBox(active=True)
    #     min_box.add_widget(check_box_5)
    #     check_box_5.group="minutes"
    #     # checkbox_5_callback = partial(self.checkbox_click,"5 mins")
    #     check_box_5.bind(active=self.checkbox_click)
    #     # check_box.bind(on_active=self.checkbox_click)

    #     # check_label_10 = Label(text = " 10  mins")
    #     # min_box.add_widget(check_label_10)
    #     # check_label_15 = Label(text = " 15  mins")
    #     # min_box.add_widget(check_label_15)
    #     # check_label_20 = Label(text = " 20  mins")
    #     # min_box.add_widget(check_label_20)
    #     # check_label_30 = Label(text = " 30  mins")
    #     # min_box.add_widget(check_label_30)
    #     # check_label_45 = Label(text = " 55  mins")
    #     # min_box.add_widget(check_label_45)
    #     # check_label_60 = Label(text = " 60  mins")
    #     # min_box.add_widget(check_label_60)
       


       
    

        
    #     # for j in range(0,12):
    #     #     check_label = Label(text = str(self.i+(j*self.i))+"   mins")
    #     #     min_box.add_widget(check_label)
    #     #     check_box = CheckBox()
    #     #     min_box.add_widget(check_box)
    #     #     check_box.id = "check"+ str(self.i+(j*self.i))
    #     #     check_box.group="minutes"
    #     #     check_box.bind(on_active=self.checkbox_click)

    #     # scroll = ScrollView(do_scroll_x=False,do_scroll_y=True, size_hint=(None, None),size=(330, 330))
    #     # scroll.add_widget(min_box)
    #     min_layout.add_widget(min_box)
    #     self.popup_time.content = min_layout
    #     self.popup_time.open()
    
    #   # Attach a callback
       
 
  
    # # # Callback for the checkbox
    # # def on_checkbox_Active(self, checkboxInstance, isActive):
    # #     if isActive:
    # #         self.lbl_active.text ="Checkbox is ON"
    # #         print("Checkbox Checked")
    # #     else:
    # #         self.lbl_active.text ="Checkbox is OFF"
    # #         print("Checkbox unchecked")

    # def checkbox_click(self,instance,isActive):
    #     if isActive:
    #         print("Checkbox Checked")
    #     else:
    #         print("Checkbox unchecked")
