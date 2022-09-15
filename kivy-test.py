import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.button import Button

import PiGPIO

io = PiGPIO.PiGPIO()

class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        

        self.button = Button(text="On")
        self.button.bind(on_press=self.turn_on)
        # self.button.bind(on_release=self.reset)
        self.button.bind(state=self.callback)
        self.add_widget(self.button)
        
        io.define_output(7)
        
    def turn_on(self, event):
        if(io.read_pin(7)):
            io.set_pin(7, False)
            self.button.background_color =(1, 0 ,0, 1)
            self.button.text = "Off"
        else:
            io.set_pin(7, True)
            self.button.background_color =(0, 1 ,0, 1)
            self.button.text = "On"
        
    def reset(self, event):
        self.label.text = "Button not Pressed"
        
    def callback(self, instance, value):
        print(f'My button {instance} state is {value}')
        
        


class MyApp(App):
    
    def build(self):
        return LoginScreen()

if __name__ == "__main__":
    MyApp().run()


