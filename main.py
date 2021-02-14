from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from UI.screen import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout

from kivy.uix.screenmanager import FadeTransition
fontk = './fonts/NanumGothic'
class KivyScreen1(Screen):
    def __init__(self, **kwargs):
        super(KivyScreen1, self).__init__(**kwargs)
        layout = GridLayout()
        layout.cols = 3
        layout.add_widget(Label(text='제목: ', font_name = fontk, font_size=30))
        self.name1 = TextInput(multiline=False)
        layout.add_widget(self.name1)

        self.press = Button()
        self.press.bind(on_release = self._pressed)
        layout.add_widget(self.press)

        self.add_widget(layout)
        '''

        self.add_widget(Label(text='내용: ', font_size=30))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='글쓴이: ', font_size=30))
        self.name = TextInput(multiline=False)
        self.test1 = Rectangle(pos=(0,0), size=(100,100))
        self.add_widget(self.name)
        '''
    def _pressed(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = '2'

class KivyScreen2(Screen):
    def __init__(self, **kwargs):
        super(KivyScreen2, self).__init__(**kwargs)
        layout = GridLayout()
        layout.cols = 3
        self.press = Button()
        self.press.bind(on_release = self._pressed)
        layout.add_widget(self.press)
        layout.add_widget(Label(text='제목2: ', font_name = fontk, font_size=30))
        self.name1 = TextInput(multiline=False)
        layout.add_widget(self.name1)



        self.add_widget(layout)
        '''

        self.add_widget(Label(text='내용: ', font_size=30))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text='글쓴이: ', font_size=30))
        self.name = TextInput(multiline=False)
        self.test1 = Rectangle(pos=(0,0), size=(100,100))
        self.add_widget(self.name)
        '''
    def _pressed(self, instance):
        self.manager.transition = FadeTransition()
        self.manager.current = '1'



class KivyApp(App):
    def build(self):
        root = ScreenManager()
        root.add_widget(KivyScreen1(name = '1'))
        root.add_widget(KivyScreen2(name = '2'))
        return root


if __name__ == '__main__':
    KivyApp().run()


if __name__ == '__main__':
    KivyApp().run()
