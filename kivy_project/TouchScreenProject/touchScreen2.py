from kivy.app import App

# from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics.vertex_instructions import Rectangle
from kivy.graphics.context_instructions import Color
from datetime import datetime
from datetime import timedelta
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty,NumericProperty
from kivy.metrics import dp
from kivy.uix.screenmanager import ScreenManager, Screen
from KivyCalendar import DatePicker

# from kivy.garden.circulardatetimepicker import CircularTimePicker
from kivy.uix.popup import Popup
from kivy.lang import Builder

# from kivymd.app import MDApp
# from kivymd.uix.picker import MDTimePicker
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.vkeyboard import VKeyboard
from kivy.factory import Factory




class Configure_cages():
    pass 

class Video_Streaming():
    pass 


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

    
    def checkbox_click(self,instance,value,cage_no):
        # print(instance)
        # print(value)
        if value == True:
            Inspection.checks.append(cage_no)
            cage_selected = ', '.join(Inspection.checks)
            self.ids.output_label.text = f'You selected: {cage_selected}'
        else:
            Inspection.checks.remove(cage_no)
            cage_selected = ', '.join(Inspection.checks)
            self.ids.output_label.text = f'You selected: {cage_selected}'

    


   

class Pagge(Popup):

    def __init__(self, **kwargs):
        super(Pagge, self).__init__(**kwargs)
        # call dismiss_popup in 1 seconds
        Clock.schedule_once(self.dismiss_popup,1)

    def dismiss_popup(self, dt):
        self.dismiss()

    def change_label(self, value):
        self.ids.text_label.text = value

    pass

class Preview(Popup):
    def dismiss_popup(self):
        self.dismiss()
        # self.show_popup()

    def saving_file(self,value):
        print(value)
        # if value == 'Animal Event':
        #     IndividualAnimalWindow().press()

        #     print(True)
        # else:
        #     print(False)
            
            # self.show_popup()
        # elif value == 'Cage Event':
        #    CageWindow().press_one()
        #    self.show_popup()
        #     # self.press_one()
        # elif value == 'Room-Level Event':
        #    RoomLevelWindow().press_two()
        #    self.show_popup()
        #     # self.press_two()
        # elif value == 'Add New Event':
        #     AddEventWindow().press_three()
        #     self.show_popup()
        #     # self.press_three()
        # else:
        #     print("there is nothing to save")

    def show_popup(self):
        Factory.Pagge().open()

   

class TimeScheduler(Popup):
    def __init__(self,**kwargs):  # my_widget is now the object where popup was called from.
        super(TimeScheduler,self).__init__(**kwargs)
    # def __init__(self, **kwargs):
    #     super(TimeScheduler, self).__init__(**kwargs)
    #     Clock.schedule_once(self.return_home_screen,1)

        # self.my_widget = my_widget

   
    text_input_str = StringProperty()

    def dismiss_popup_1(self):
        self.dismiss()

    def return_home_screen(self):
        pass

    def get_time_to_spent(self):
        self.text_input_str = self.ids.timespen.text
        # if self.ids.timespen.text.isnumeric():
        #     self.text_input_str = self.ids.timespen.text
        # else:
        #     self.text_input_str = 0

        # print(self.ids.timespen.hint_text)
        # print(self.text_input_str)
        return self.text_input_str

    
    
class WelcomePage(Screen):

    time_on_next_button = ObjectProperty()
    time_spent = ObjectProperty()
    def get_time(self):
        self.time_on_next_button = datetime.now()
        self.time_on_next_button = self.time_on_next_button.strftime("%H:%M:%S")
        # print(datetime.now())
        # print(self.time_on_next_button)

    def show_popup_2(self):
       Factory.TimeScheduler().open()
       self.time_spent = Factory.TimeScheduler().get_time_to_spent()
       print(self.time_spent)


    # def check_current_time(self):
    #     print("okay1")
    #     print(Factory.TimeScheduler().get_time_to_spent())
    #     print("okay")
        # if datetime.now() == self.time_on_next_button+timedelta(minutes=TimeScheduler().get_time_to_spent()):
        #     print("okay")
        # else:
        #     print("not okay")
    pass


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
    recorded_by = ObjectProperty(None)
    anim_type = ObjectProperty(None)
    length = ObjectProperty(None)

    def press(self):
        cage_number = self.cage_number
        animal_id = self.animal_id
        event_category = self.event_category
        duration = self.duration
        date = self.date
        weight = self.weight
        dosage = self.dosage
        description = self.description
        recorded_by = self.recorded_by
        anim_type = self.anim_type
        length = self.length
        with open("AnimalRecords.txt", mode="a") as myfile:
            myfile.writelines(
                f"Cage Number: {cage_number.text}\nAnimal ID: {animal_id.text}\nEvent Category: {event_category.text}\nDuration: {duration.text}\nDate: {date.text}\nWeight: {weight.text}\nLength: {length.text}\nDosage: {dosage.text}\nDescription: {description.text}\nRecorded_by: {recorded_by.text}\nType: {anim_type.text}\n\n"
            )
            print(
                "Cage No: ",
                cage_number.text,
                "\nanimal_id: ",
                animal_id.text,
                "\nevent_category: ",
                event_category.text,
                "\nduration: ",
                duration.text,
                "\ndate: ",
                date.text,
                "\nweight: ",
                weight.text,
                "\ndosage: ",
                dosage.text,
                "\ndescription: ",
                description.text,
                "\nrecorded_by: ",
                recorded_by.text,
                "\nroom_type: ",
                anim_type.text,
                "\nlength: ",
                length.text,
                "\nADDED!",
            )

        self.cage_number = ""
        self.animal_id = ""
        self.event_category = ""
        self.duration = ""
        self.date = ""
        self.weight = ""
        self.dosage = ""
        self.description = ""
        self.recorded_by = ""
        self.anim_type = ""
        self.length = ""

    # spinner drop down for type of event 
    def spinner_clicked(self, value):
        self.ids.anim_type.text = value
        pass
    
    # spinner drop down for animals by color 
    def spinner_clicked_anim(self, value1):
        self.ids.animal_id.text = value1
        pass
    
    # def show_popup(self):
    #     Factory.Pagge().open()

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def show_popup_1(self):
           Factory.Preview().open()

    pass


class CageWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_clock, 1)
        show = Pagge()

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
    recorded_by = ObjectProperty(None)
    cage_type = ObjectProperty(None)

    def press_one(self):
        cage_number = self.cage_number
        event_category = self.event_category
        duration = self.duration
        date = self.date
        description = self.description
        recorded_by = self.recorded_by
        cage_type = self.cage_type

        with open("CageRecords.txt", mode="a") as myfile:
            myfile.writelines(
                f"Cage Number: {cage_number.text}\nEvent Category: {event_category.text}\nDuration: {duration.text}\nDate: {date.text}\nDescription: {description.text}\nRecorded_by: {recorded_by.text}\nType: {cage_type.text}\n\n"
            )
            print(
                "Cage No: ",
                cage_number.text,
                "\nevent_category: ",
                event_category.text,
                "\nduration: ",
                duration.text,
                "\ndate: ",
                date.text,
                "\ndescription: ",
                description.text,
                "\nrecorded_by: ",
                recorded_by.text,
                "\nroom_type: ",
                cage_type.text,
                "\nADDED!",
            )

        self.cage_number = ""
        self.event_category = ""
        self.duration = ""
        self.date = ""
        self.description = ""
        self.recorded_by = ""
        self.cage_type = ""

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def spinner_clicked(self, value):
        self.ids.cage_type.text = value

    # def show_popup(self):
    #     Factory.Pagge().open()

    def show_popup_1(self):
           Factory.Preview().open()


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
    recorded_by = ObjectProperty(None)
    room_type = ObjectProperty(None)

    def press_two(self):
        event_category = self.event_category
        duration = self.duration
        date = self.date
        description = self.description
        recorded_by = self.recorded_by
        room_type = self.room_type

        with open("RoomRecords.txt", mode="a") as myfile:
            myfile.writelines(
                f"Event Category: {event_category.text}\nDuration: {duration.text}\nDate: {date.text}\nDescription: {description.text}\nRecorded_by: {recorded_by.text}\nType: {room_type.text}\n\n"
            )
            print(
                "event_category: ",
                event_category.text,
                "\nduration: ",
                duration.text,
                "\ndate: ",
                date.text,
                "\ndescription: ",
                description.text,
                "\nrecorded_by: ",
                recorded_by.text,
                "\nroom_type: ",
                room_type.text,
                "\nADDED!",
            )

        self.event_category = ""
        self.duration = ""
        self.date = ""
        self.description = ""
        self.recorded_by = ""
        self.room_type = ""

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    def spinner_clicked(self, value):
        self.ids.room_type.text = value
        pass
    

    # def show_popup(self):
    #     Factory.Pagge().open()

    
    def show_popup_1(self):
       Factory.Preview().open()      

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
    duration = ObjectProperty(None)
    date = ObjectProperty(None)
    description = ObjectProperty(None)
    created_by = ObjectProperty(None)

    def spinner_clicked(self, value):
        self.ids.event_category.text = value
        pass

    def press_three(self):
        event_category = self.event_category
        event_name = self.event_name
        date = self.date
        time = self.time
        description = self.description
        created_by = self.created_by
        with open("AddEventRecords.txt", mode="a") as myfile:
            myfile.writelines(
                f"Event Category: {event_category.text}\nEvent Name: {event_name.text}\nDate: {date.text}\nTime: {time.text}\nDescription: {description.text}\nCreated_by: {created_by.text}\n\n"
            )
            print(
                "event_category: ",
                event_category.text,
                "\nduration: ",
                event_name.text,
                "\ndate: ",
                date.text,
                "\ntime: ",
                time.text,
                "\ndescription: ",
                description.text,
                "created_by: ",
                created_by.text,
                "\nADDED!",
            )

        self.event_category = ""
        self.event_name = ""
        self.date = ""
        self.time = ""
        self.description = ""
        self.created_by = ""

    def update_clock(self, *args):
        # Called once a second using the kivy.clock module
        # Add one second to the current time and display it on the label
        self.now = self.now + timedelta(seconds=1)
        self.my_text_2 = self.now.strftime("%H:%M:%S")

    pass

    # def show_popup(self):
    #     Factory.Pagge().open()

    def show_popup_1(self):
        Factory.Preview().open()

    # def key_up(self, keyboard, keycode, *args):
    #     if isinstance(keycode, tuple):
    #         print(keycode)
    #         keycode = keycode[1]

    #         prev_text = self.root.ids.time.text

    #         self.root.ids.time.text = f"{prev_text} {keycode}"
    #     pass


class EventCategoryWindow(Screen):
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


class WindowManager(ScreenManager):
    my_global = StringProperty()
    cage_ids = StringProperty()
   


    # event_cat = my_global

    # print(my_global)

    # def saving_file(self):
    #     print(self.ids.my_global)
        # if self.ids.my_global == 'Animal Event':
        #     self.press()
        # elif self.ids.my_global == 'Cage Event':
        #     self.press_one()
        # elif self.ids.my_global == 'Room Level Event':
        #     self.press_two()
        # elif self.ids.my_global == 'Add New Event':
        #     self.press_three()
        # else:
        #     print("there is nothing to save")


    pass

  

class keyboardLayout(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = GridLayout(cols=1)

        # self.label = Label(text='Type Something')

        keyboard = VKeyboard(on_key_up=self.key_up)

        # layout.add_widget(self.label)

        layout.add_widget(keyboard)

    def key_up(self, keyboard, keycode, *args):
        if isinstance(keycode, tuple):
            print(keycode)
            keycode = keycode[1]

        prev_text = self.label.text

        if prev_text == "Type Something":
            prev_text = ""

        # Backspace
        if keycode == "backspace":
            prev_text = prev_text[:-1]
            keycode = ""
        # SpaceBar
        if keycode == "spacebar":
            keycode = " "
        # Enter
        if keycode == "enter":
            keycode = "\n"
        # Tab
        if keycode == "tab":
            keycode = "\t"

        # update label
        self.label.text = f"{prev_text}{keycode}"


class FirstApp(App):
    title = "Record"
    def build(self):
        self.sm = WindowManager()
        return self.sm
       

    # pass
    # def build(self):
    #     layout = GridLayout(cols=1)

    #     keyboard = VKeyboard(on_key_up=self.key_up)

    #     self.label = Label(text='Type Something')

    #     layout.add_widget(self.label)

    #     layout.add_widget(keyboard)
    #     return layout

    # def key_up(self, keyboard, keycode, *args):
    #     if isinstance(keycode, tuple):
    #         print(keycode)
    #         keycode = keycode[1]

    #     prev_text = self.label.text

    #     if prev_text == 'Type Something':
    #         prev_text = ''

    #     #Backspace
    #     if keycode == 'backspace':
    #         prev_text = prev_text[:-1]
    #         keycode = ''
    #     #SpaceBar
    #     if keycode == 'spacebar':
    #         keycode = ' '
    #     #Enter
    #     if keycode == 'enter':
    #         keycode = '\n'
    #     #Tab
    #     if keycode == 'tab':
    #         keycode = '\t'

    # #update label
    # self.label.text = f'{prev_text}{keycode}'


if __name__ == "__main__":
    FirstApp().run()

