from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.label import BoxLayout

def tst():
    print('KIKI')

class MyApp(App):
    def build(self):
        txt = Label(text ='Это надпись' )
        btn = Button(text = 'Это кнопка')
        btn.on_press = tst

        layot = BoxLayout()
        layot.add_widget(txt)
        layot.add_widget(btn)
        return layot
MyApp.run()