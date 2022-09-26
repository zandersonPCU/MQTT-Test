import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout

from functools import partial

from PiGPIO import PiGPIO

io = PiGPIO()

Config.set('graphics',  'fullscreen', '1')
Config.write()

class MainPage(GridLayout):
    
    def __init__(self, **kwargs):
        super(MainPage, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 2
        
        
        self.button_box = BoxLayout(orientation="horizontal")

        self.pin_7_label = Label(text="Pin 7 Button:")
        self.button_box.add_widget(self.pin_7_label)

        self.button = Button(text="On")
        self.button.bind(on_press=partial(self.turn_on, pin_num=7))
        # self.button.bind(on_release=self.reset)
        self.button.bind(state=self.callback)
        self.button_box.add_widget(self.button)

        self.button_box_2 = BoxLayout(orientation="horizontal")
        self.pin_11_label = Label(text="Pin 11 Button:")
        self.button_box_2.add_widget(self.pin_11_label)
        self.pin_11_button = Button(text="On")
        self.pin_11_button.bind(on_press=partial(self.turn_on, pin_num=11))
        self.button_box_2.add_widget(self.pin_11_button)
        
        self.add_widget(self.button_box)
        self.add_widget(self.button_box_2)


        io.define_output(7)
        io.define_output(11)
        
    def turn_on(self, instance, pin_num):
        if(io.read_pin(pin_num)):
            io.set_pin(pin_num, False)
            instance.background_color =(1, 0 ,0, 1)
            instance.text = "Off"
        else:
            io.set_pin(pin_num, True)
            instance.background_color =(0, 1 ,0, 1)
            instance.text = "On"
        
    def callback(self, instance, value):
        print(f'My button {instance} state is {value}')


class MyApp(App):
    
    def build(self):
        return MainPage()

if __name__ == "__main__":
    MyApp().run()


