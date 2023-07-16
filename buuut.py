from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen 

class ScrButton(Button):
    def __init__(self, screen, direction,goal,**kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
    def on_press(self):
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current =self.goal

class MainScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        vl = BoxLayout(orientation='vertical',padding = 8, spacing=8)
        hl = BoxLayout()
        txt = Label(text = 'Выбери экран')
        vl.add_widget(ScrButton(self,direction='down',goal = 'first',text = '1'))
        vl.add_widget(ScrButton(self,direction='up',goal ='second',text = '2'))
        hl.add_widget(txt)
        hl.add_widget(vl)
        self.add_widget(hl)
class FirstScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        vl = BoxLayout(orientation = 'vertical',size_hint = (0.5,0.5),pos_hint = {'center_x': 0.5,'center_y':0.5})
        btn = Button(text = 'Выбор:1',size_hint = (0.5,1),pos_hint = {'left':0})
        btn_back = ScrButton(self,direction='up',goal = 'main', text = 'Назад',size_hint = (0.5,1), pos_hint = {'right': 1})
        vl.add_widget(btn)
        vl.add_widget(btn_back)
        self.add_widget(vl)

class ThirdScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        layout = BoxLayout(orientatiom = 'vertical')
        btn_back = ScrButton(self,direction = 'down',goal = 'main', text = 'Назад',size_hint= (1,None),height= '40sp')
        test_label = Label(text = 'Твой собственный экран')
        layout.add_widget(btn_back)
        self.add_widget(layout)

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainScr(name = 'main'))
        sm.add_widget(FirstScr(name = 'first'))
        sm.add_widget(ThirdScr(name = 'third'))
        return sm
MyApp().run()