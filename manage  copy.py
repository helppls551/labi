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
        animate = Animation(background_color = (0,0,1,1), color = (1,1,0,1),
        font_size = 18, duration = 1.5)

        animate = animate + Animation(background_color=(1,1,0,1),duration = 1.5)
        animate = animate + Animation(pos_hint = {'center_x': 1.1},background_color = (0,0,1,1))
        animate = animate + Animation(pos_hint = {'center_x': 0.1},background_color = (0,0,1,1),
        duration = 0.5)

        back = Animation(background_color = start_color,size_hint = start_size_h,pos_hint = start_pos_hint,
        color = start_c, font_size = size)

        self.animate = animate +back

    def start_animation(self):
        self.animate.start(self)
        app.convert()
class MyApp(App):
    def build(self):
        self.withconvert = 'RUB'
        self.toconvert = 'RUB'
        self.layout = BoxLayout(orientation ='vertical')
        
        self.img = Image(source = 'money.png')
        self.layout.add_widget(self.img)
        self.t_text = Label(text = '0',color = '#098000',font_size = 45)
        self.layout.add_widget(self.t_text)
        self.groupMain = BoxLayout()
        self.lefttext = Label(text = 'Конвертация с')
        self.btnUSDwith = Button(text = 'USD')
        self.btnRUBwith = Button(text = 'RUB')
        self.btnEURwith = Button(text = 'EUR')
        self.btngroup1 = BoxLayout(orientation = 'vertical')
        self.btngroup1.add_widget(self.lefttext)
        self.btngroup1.add_widget(self.btnUSDwith)
        self.btngroup1.add_widget(self.btnRUBwith)
        self.btngroup1.add_widget(self.btnEURwith)
        self.btnUSDwith.on_press = self.usdwith
        self.btnRUBwith.on_press = self.rubwith
        self.btnEURwith.on_press = self.eurwith

        self.righttext = Label(text = 'Конвертация в')
        self.btnRUBto =  Button(text = 'RUB')
        self.btnUSDto = Button(text = 'USD')
        self.btnEURto = Button(text = 'EUR')
        self.btngroup2 = BoxLayout(orientation = 'vertical')
        self.btngroup2.add_widget(self.righttext)
        self.btngroup2.add_widget(self.btnRUBto)
        self.btngroup2.add_widget(self.btnUSDto)
        self.btngroup2.add_widget(self.btnEURto)
        self.btnUSDto.on_press = self.usdto
        self.btnRUBto.on_press = self.rubto
        self.btnEURto.on_press = self.eurto
        self.toconvert = ''

        self.groupMain.add_widget(self.btngroup1)
        self.groupMain.add_widget(self.btngroup2)

        self.layout.add_widget(self.groupMain)
        
        self.write_valute = TextInput(size_hint = (1,0.2))
        self.layout.add_widget(self.write_valute)
        self.layout_down = BoxLayout()
        self.btn = AnimatedButton(text = 'Конвертация', size_hint=(0.3, 0.2),pos_hint = {'center_x': 0.5})
        self.conv = 0
        self.lab = Label(text = f'Конвертаций:{self.conv}',size_hint=(0.3, 0.2),pos_hint = {'center_x': 0.5})
        self.layout_down.add_widget(self.btn)
        self.layout_down.add_widget(self.lab)
        self.layout.add_widget(self.layout_down)
        self.btn.on_press = self.btn.start_animation

        return self.layout
    # def conv(self):
    #     self.pop = Popup(title = 'Счетчик', content = Label(text = f'Конвертаций: {self.conv}'),
    #          size_hint = (None,None), size = (500,500), pos_hint = {'center_x': 0.5,'center_y': 0.5})
    #     self.pop.open()
    def convert(self):
        if self.write_valute.text  =='': 
            self.write_valute.text = '0'
        elif self.write_valute.text == '666':
            self.withconvert = 'USD'
            self.toconvert = 'USD'
            popup = Popup(title = 'пасахалка', content = Label(text = 'пасхалочка'),
            size_hint = (None,None), size = (500,500), pos_hint = {'center_x': 0.5,'center_y': 0.5})
            popup.open()
            self.lab = Label(text = f'Конвертаций:{self.conv}:)',size_hint=(0.3, 0.2),pos_hint = {'center_x': 0.5})
        else:
            self.conv += 1
            self.lab.text =  f'Конвертаций:{str(self.conv)}:)'
        if self.withconvert == 'USD' and self.toconvert == 'RUB':
            self.t_text.text = str(94.20 * float(self.write_valute.text)) + 'RUB'
            
        elif self.withconvert == 'USD' and self.toconvert == 'USD':
            self.t_text.text = str(self.write_valute.text) + 'USD'
            
        elif self.withconvert == 'RUB' and self.toconvert == 'USD':
            self.t_text.text = str(0.01 *float(self.write_valute.text)) +'USD'
            
        elif self.withconvert == 'RUB' and self.toconvert == 'RUB':
            self.t_text.text = str(self.write_valute.text) + 'RUB'
            
        elif self.withconvert == 'EUR' and self.toconvert == 'USD':
            self.t_text.text = str(1.09 * float(self.write_valute.text)) + 'USD'
            
        elif self.withconvert == 'EUR' and self.toconvert == 'RUB':
            self.t_text.text = str(101.48 * float(self.write_valute.text)) + 'RUB'
            
        elif self.withconvert == 'USD' and self.toconvert == 'EUR':
            self.t_text.text = str(0.92 * float(self.write_valute.text)) + 'EUR'
            
        elif self.withconvert == 'RUB' and self.toconvert == 'EUR':
            self.t_text.text == str(0.009 * float(self.write_valute.text)) + ' EUR'
            
        elif self.withconvert == 'EUR' and self.toconvert == 'EUR':
            self.t_text.text = str(self.write_valute.text) + 'EUR'
            
        else:
            popup = Popup(title = 'Инструкция!!!', content = Label(text = txt),
            size_hint = (None,None), size = (500,500), pos_hint = {'center_x': 0.5,'center_y': 0.5})
            popup.open()  
    def usdwith(self):
        self.withconvert = 'USD'
    
    def rubwith(self):
        self.withconvert ='RUB'
    
    def eurwith(self):
        self.withconvert = 'EUR'
    
    def usdto(self):
        self.toconvert = 'USD'
    
    def rubto(self):
        self.toconvert = 'RUB'

    def eurto(self):
        self.toconvert = 'EUR'

txt = '''Выберите конвертируемую валюту в левой стороне,
в правой стороне выберите валюту, которую хотите
получить, затем в текстовое поле напишите количество
и нажмите кнопку "Конвертация"!
'''
app = MyApp()
app.run()