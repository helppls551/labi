from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.animation import Animation
from kivy.uix.popup import Popup
from kivy.core.window import Window
Window.clearcolor = (0.70,0.35,0.35,1)

class AnimatedButton (Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        start_color = self.background_color
        start_size_h = self.size_hint
        start_pos_hint = self.pos_hint
        start_c = self.color
        size = self.font_size

        animate = animate + Animation(background_color=(1,1,0,1),duration = 1.5)
        animate = animate + Animation(pos_hint = {'center_x': 1.1},background_color = (0,0,1,1))
        animate = animate + Animation(pos_hint = {'center_x': 0.1},background_color = (0,0,1,1),
        duration = 0.5)
        back = Animation(background_color = start_color,size_hint = start_size_h,pos_hint = start_pos_hint,
        color = start_c, font_size = size)

        self.animate = animate +back
    def start_animation(self):
        self.animate.start(self)
        App.convert()
class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation ='vertical')
        
        self.img = Image(source = 'money.png')
        self.layout.add_widget(self.img)
        self.t_text = Label(text = '0',color = '#098000',font_size = 45)
        self.layout.add_widget(self.t_text)
        self.groupMain = BoxLayout()
        self.lefttext = Label(text = 'Конвертация с')
        self.btnUSDwith = Button(text = 'USD')
        self.btnRUBwith = Button(text = 'RUB')
        self.btngroupl = BoxLayout(orientation = 'vertical')