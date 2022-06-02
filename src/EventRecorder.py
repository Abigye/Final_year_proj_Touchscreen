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
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
from kivy.graphics.texture import Texture
from Helperfunctions import write_to_text_file, videos, file_to_view
import cv2
import random
import os
import sys
from kivy.resources import resource_add_path


class ViewRecordedEvents(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1,
                            size_hint_y=None, size_hint_x=1,
                            row_default_height=200)
        # row_force_default=True)
    # Make sure the height is such that there is something to scroll.
        layout.bind(minimum_height=layout.setter('height'))

        records = file_to_view()
        if len(records) != 0:
            for record in records:
                grid = GridLayout(cols=1, rows=len(record))
                layout.add_widget(Label(text=''))
                for i in record:
        
                    label = Label(text=(i), padding= ("6dp", "6dp"))
                   
                    # label.bind(size=label.setter('texture_size'))
                    # label.bind(text_size =label.setter('(width,None)'))
                    grid.add_widget(label)

                layout.add_widget(grid)
        else:
            layout.add_widget(
                Label(text="Nothing to display", pos_hint=(0.5, 0.5)))

        
        # def create_Label(self,tex):
        #     t_label = Label(text=tex, text_size=(self.width,None),size=self.texture_size)
        #     return t_label

        root = ScrollView()
        root.add_widget(layout)
        # box_layout.add_widget(root)
        self.add_widget(root)


class FirstScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        Clock.schedule_interval(self.recv_1, 1.0/30.0)
        Clock.schedule_interval(self.recv_2, 1.0/30.0)
        Clock.schedule_interval(self.recv_3, 1.0/30.0)
        Clock.schedule_interval(self.recv_4, 1.0/30.0)

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

    video_1 = cv2.VideoCapture(videos[0])
    video_2 = cv2.VideoCapture(videos[1])
    video_3 = cv2.VideoCapture(videos[2])
    video_4 = cv2.VideoCapture(videos[3])

    def recv_1(self, *args):
        ret, frame = self.video_1.read()
        if ret:
            # flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video = self.ids.image_source
            video.texture = image_texture
        else:
            self.video_1.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def recv_2(self, *args):
        ret, frame = self.video_2.read()
        if ret:
            # flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video_21 = self.ids.image_source_1
            video_21.texture = image_texture

        else:
            self.video_2.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def recv_3(self, *args):
        ret, frame = self.video_3.read()
        if ret:
            # flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video_22 = self.ids.image_source_2
            video_22.texture = image_texture

        else:
            self.video_3.set(cv2.CAP_PROP_POS_FRAMES, 0)

    def recv_4(self, *args):
        ret, frame = self.video_4.read()
        if ret:
            # flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video_23 = self.ids.image_source_3
            video_23.texture = image_texture
        else:
            self.video_4.set(cv2.CAP_PROP_POS_FRAMES, 0)


class VideoEx(Screen):
    def __init__(self, **kwargs):
        super(VideoEx,self).__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        # selected_video = random.choice(videos)
        # capture = cv2.VideoCapture(selected_video)
        # self.ids.image_source = capture.release()

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
        bigger_box = GridLayout(rows=2, spacing=10)
        box = GridLayout(cols=2)
        box.add_widget(Label(text="IpAddress: "))
        self.st = TextInput(text="")
        box.add_widget(self.st)
        box.add_widget(Label(text="Port: "))
        self.pt = TextInput(text="")
        box.add_widget(self.pt)
        bigger_box.add_widget(box)
        set_box = GridLayout(cols=3, size_hint_y=None,
                             height=50)
        set_box.add_widget(Label(text=""))
        btn = Button(text="Set", background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.setProcess)
        set_box.add_widget(btn)
        set_box.add_widget(Label(text=""))
        bigger_box.add_widget(set_box)
        self.popup = Popup(
            title='Settings', content=bigger_box, size_hint=(.6, .4))
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

    selected_video = random.choice(videos)
    capture = cv2.VideoCapture(selected_video)
    # self.ids.image_source = capture.release()

    def playPause(self):
        if self.ids.play_stop_btn.text == "Stop":
            self.ids.play_stop_btn.background_color = (0, 0, 1, 1)
            self.ids.play_stop_btn.text = 'Play'
            self.capture.release()
            # cv2.destroyAllWindows()
            self.ids.image_source.reload()
            # cv2.waitKey(0)

        else:
            self.ids.play_stop_btn.text = "Stop"
            self.ids.play_stop_btn.background_color = (1, 0, 0, 1)
            Clock.schedule_interval(self.recv, 1.0/30.0)

    def recv(self, *args):
        # myrtmp_addr = "rtmp://myip:1935/myapp/mystream"
        ret, frame = self.capture.read()
        if ret:
            # flip upside down
            buf = cv2.flip(frame, 0)
            image_texture = Texture.create(
                size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            image_texture.blit_buffer(
                buf.tostring(), colorfmt='bgr', bufferfmt='ubyte')
            video = self.ids.image_source
            video.texture = image_texture


class RecordRackEvent(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)

    my_text = StringProperty("0")
    my_text_2 = StringProperty("0")

    # datetime object containing current date and time
    now = datetime.now()
    my_text = now.strftime("%B %d, %Y")

    event_category = ObjectProperty(None)
    start_time = ObjectProperty(None)
    end_time = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    rack_type = ObjectProperty(None)
    cages_selected = ObjectProperty(None)

    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(300, 300))

    def onPressFinish(self):
        layout = GridLayout(rows=6, padding=10)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        box.add_widget(Label(text=""))
        SaveExitButton = Button(text="Save", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release=self.change_screen_to_welcome)

    def press(self, EditButton):
        write_to_text_file(Event_category=self.event_category.text, Selected_cages=self.cages_selected.text, Start_time=self.start_time.text, End_time=self.end_time.text, Date=self.date.text,
                           Description=self.description.text, Type=self.rack_type.text)

    def change_screen_to_welcome(self, EditButton):
        self.manager.current = 'first_screen'
        self.manager.transition.direction = 'left'

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def spinner_clicked(self, value):
        self.ids.rack_type.text = value


class Inspection(Screen):
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

    def change_screen_to_welcome(self, NoButton):
        self.manager.current = 'first_screen'
        self.manager.transition.direction = 'left'

    def check_selected_cage_for_video(self, text_to_show):

        popup_view = Popup(title='View cage', size_hint=(
            None, None), size=(400, 200))

        layout_pop = GridLayout(rows=5)
        layout_pop.add_widget(Label(text=""))
        popupLabel = Label(text=text_to_show)
        layout_pop.add_widget(popupLabel)
        layout_pop.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout_pop.add_widget(box)
        backButton = Button(text="Back", background_color=(0, 0, 1, 1))
        box.add_widget(Label(text=""))
        box.add_widget(backButton)
        box.add_widget(Label(text=""))
        popup_view.content = layout_pop
        popup_view.open()
        backButton.bind(on_press=popup_view.dismiss)

    output_label = ObjectProperty(None)

    def changing_color_of_view_cage(self):
        cages = self.output_label.text.split(":")
        if len(cages) <= 1:
            self.check_selected_cage_for_video(
                "Please select one cage to view")
        else:
            print(cages[1])
            if cages[1] == " ":
                self.check_selected_cage_for_video(
                    "Please select one cage to view")
            else:
                number_of_selected_cages = cages[1].split(",")
                if number_of_selected_cages[0] == ' No cages' or len(number_of_selected_cages) != 1 or number_of_selected_cages[0] == " ":
                    self.check_selected_cage_for_video(
                        "Only one cage can be viewed at a time")
                else:
                    self.manager.current = "video_to_play"
                    self.manager.transition.direction = 'left'

    multiselected_btns = []
    blue_color = [0, 0, 1, 1]
    no_color = [1, 1, 1, 1]

    def multiselecting_btns(self, btn_id, cage_no):
        btns_selected = ""
        if btn_id.background_color != self.blue_color:
            Inspection.multiselected_btns.append(cage_no)
            btn_id.background_color = self.blue_color
        else:
            Inspection.multiselected_btns.remove(cage_no)
            btn_id.background_color = self.no_color

        btns_selected = ", ".join(Inspection.multiselected_btns)
        self.output_label.text = f"You selected: {btns_selected}"

        print(", ".join(Inspection.multiselected_btns))

    def select_all_btns(self):
        all_btn_ids = [self.ids.btn_1, self.ids.btn_2, self.ids.btn_3,
                       self.ids.btn_4, self.ids.btn_5, self.ids.btn_6,
                       self.ids.btn_7, self.ids.btn_8, self.ids.btn_9,
                       self.ids.btn_10, self.ids.btn_11, self.ids.btn_12]
        if self.ids.select_all_btn.text == "Select All":
            self.ids.select_all_btn.text = "Deselect All"
            for btnid in all_btn_ids:
                if btnid.background_color != self.blue_color and btnid.text not in Inspection.multiselected_btns:
                    btnid.background_color = self.blue_color
                    Inspection.multiselected_btns.append(btnid.text)
        elif self.ids.select_all_btn.text == "Deselect All":
            self.ids.select_all_btn.text = "Select All"
            for btnid in all_btn_ids:
                if btnid.background_color == self.blue_color:
                    self.output_label.text = "You selected: "
                    btnid.background_color = self.no_color
                    Inspection.multiselected_btns.remove(btnid.text)
        btn_texts = ", ".join(Inspection.multiselected_btns)
        self.output_label.text = f"You selected: {btn_texts}"

    def display(self):
        selected_cages_from_rack = self.manager.get_screen("rack")
        if self.output_label.text == "" or self.output_label.text == None:
            self.output_label.text = "No cage selected"
            selected_cages_from_rack.ids.cages_selected.text = self.output_label.text
        else:
            selected_cages_from_rack.ids.cages_selected.text = self.output_label.text.split(":")[
                1]


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
    end_time = ObjectProperty(None)
    start_time = ObjectProperty(None)
    date = ObjectProperty(None)
    weight = ObjectProperty(None)
    dosage = ObjectProperty(None)
    description = ObjectProperty(None)
    anim_type = ObjectProperty(None)
    length = ObjectProperty(None)

    popup = Popup(title='Animal IDs', size_hint=(None, None), size=(400, 300))

    def get_all_animal_ids(self):
        all_animal_ids = ["98900102505680" + str(i) if len(
            str(i)) == 1 else "9890010250568" + str(i) for i in range(1, 37)]
        return all_animal_ids

    def get_animal_ids_for_cage(self, value):
        num = int(value.split()[1])
        if num == 1:
            animal_ids_for_selected_cage = self.get_all_animal_ids()[0:4]
        else:
            animal_ids_for_selected_cage = self.get_all_animal_ids()[
                ((num-1)*3)-1:num*3]

        return animal_ids_for_selected_cage

    def select_id(self):
        pop_layout = GridLayout(cols=1)
        box = GridLayout(cols=1, spacing=4, padding=5, size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))

        for i in self.get_animal_ids_for_cage(self.cage_number.text):
            btn1 = Button(text=i, size_hint_x=0.2, size_hint_y=None, height=50)

            box.add_widget(btn1)
            btn1.bind(on_press=self.callback)
            btn1.bind(on_release=self.popup.dismiss)

        scroll = ScrollView(do_scroll_x=False, do_scroll_y=True,
                            size_hint=(None, None), size=(300, 200))
        scroll.add_widget(box)
        pop_layout.add_widget(scroll)
        self.popup.content = pop_layout
        self.popup.open()

    def callback(self, instance):
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
        size=(300, 300))

    def onPressFinish(self):
        layout = GridLayout(rows=6, padding=10)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        box.add_widget(Label(text=""))
        SaveExitButton = Button(text="Save", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release=self.change_screen_to_welcome)

    def press(self, EditButton):
        write_to_text_file(Cage_number=self.cage_number.text, Animal_ID=self.animal_id.text, Event_category=self.event_category.text,
                           Start_time=self.start_time.text, End_time=self.end_time.text, Date=self.date.text, Weight=self.weight.text, Length=self.length.text,
                           Dosage=self.dosage.text, Description=self.description.text, Type=self.anim_type.text)

    def change_screen_to_welcome(self, EditButton):
        self.manager.current = 'first_screen'
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
    start_time = ObjectProperty(None)
    end_time = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    cage_type = ObjectProperty(None)

    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(300, 300))

    def onPressFinish(self):
        layout = GridLayout(rows=6, padding=10)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        box.add_widget(Label(text=""))
        SaveExitButton = Button(text="Save", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release=self.change_screen_to_welcome)

    def press(self, EditButton):
        write_to_text_file(Cage_number=self.cage_number.text, Event_category=self.event_category.text, Start_time=self.start_time.text, End_time=self.end_time.text, Date=self.date.text,
                           Description=self.description.text, Type=self.cage_type.text)

    def change_screen_to_welcome(self, EditButton):
        self.manager.current = 'first_screen'
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
    end_time = ObjectProperty(None)
    start_time = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    room_type = ObjectProperty(None)

    popup_finish = Popup(
        title="Preview and Save Record",
        size_hint=(None, None),
        size=(300, 300))

    def onPressFinish(self):
        layout = GridLayout(rows=6, padding=10)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        popupLabel = Label(text="Do you want to edit record before saving?")
        layout.add_widget(popupLabel)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        box.add_widget(Label(text=""))
        SaveExitButton = Button(text="Save", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_press=self.press)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release=self.change_screen_to_welcome)

    def press(self, EditButton):
        write_to_text_file(Event_category=self.event_category.text, Start_time=self.start_time.text, End_time=self.end_time.text, Date=self.date.text,
                           Description=self.description.text, Type=self.room_type.text)

    def change_screen_to_welcome(self, EditButton):
        self.manager.current = 'first_screen'
        self.manager.transition.direction = 'left'

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    popup_type = Popup(title='Room Level Event Types',
                       size_hint=(None, None), size=(400, 300))

    def spinner_clicked(self, value):
        self.ids.room_type.text = value


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
        size=(300, 300))

    # saves the record upon clicking the finish button

    def onPressFinish(self):
        layout = GridLayout(rows=6, padding=10)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        popupLabel = Label(
            text="Do you want to edit the new type before\nsaving?")
        layout.add_widget(popupLabel)
        layout.add_widget(Label(text=""))
        layout.add_widget(Label(text=""))
        box = GridLayout(cols=3)
        layout.add_widget(box)
        EditButton = Button(text="Edit")
        box.add_widget(EditButton)
        box.add_widget(Label(text=""))
        SaveExitButton = Button(text="Save", background_color=(0, 1, 0, 1))
        box.add_widget(SaveExitButton)
        self.popup_finish.content = layout
        self.popup_finish.open()

        # Attach close button press with popup.dismiss action
        EditButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_press=self.add_to_event_cat)
        SaveExitButton.bind(on_press=self.popup_finish.dismiss)
        SaveExitButton.bind(on_release=self.change_screen_to_welcome)

    # adds a newly created event to its selected event category
    def add_to_event_cat(self, EditButton):
        screen_to_update = None
        if self.event_category.text == 'Individual Animal' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen(
                "animal").anim_type.values.append(self.event_name.text)
        elif self.event_category.text == 'Cage' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen(
                "cage").cage_type.values.append(self.event_name.text)
        elif self.event_category.text == 'Room Level' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen(
                "room").room_type.values.append(self.event_name.text)
        elif self.event_category.text == 'Rack' and self.event_name.text != '':
            self.screen_to_update = self.manager.get_screen(
                "rack").rack_type.values.append(self.event_name.text)

    def change_screen_to_welcome(self, EditButton):
        self.manager.current = 'first_screen'
        self.manager.transition.direction = 'left'

    def get_values_for_event_category(self, value):
        self.ids.event_type_label.text = 'Event type present for '
        if value == 'Individual Animal':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + \
                ', '.join(self.manager.get_screen("animal").anim_type.values)
        elif value == 'Cage':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(
                self.manager.get_screen("cage").cage_type.values)
        elif value == 'Room Level':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(
                self.manager.get_screen("room").room_type.values)
        elif value == 'Rack':
            self.ids.event_type_label.text += self.event_category.text + ' are \n' + ', '.join(
                self.manager.get_screen("rack").rack_type.values)

        print("cat= " + self.ids.event_type_label.text)


class WindowManager(ScreenManager):
    my_global = StringProperty("")
    cage_ids = StringProperty("")
    selected_cages = StringProperty("")

    pass


class EventRecorderApp(App):
    title = "ACTUALHCA EVENT RECORDER"

    def build(self):
        self.sm = WindowManager()
        return self.sm


if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    EventRecorderApp().run()
