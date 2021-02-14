from kivy.uix.screenmanager import Screen as kivy_Screen

class Screen(kivy_Screen):
    layout = None
    widget_list = []
    def __init__(self, **kwargs):
        super(kivy_Screen, self).__init__(**kwargs)

    def set_widget(self, widget_list):
        self.widget_list = widget_list

    def set_layout(self, layout):
        self.layout = layout
        for widget in self.widget_list:
            self.layout.add_widget(widget)

        self.add_widget(self.layout)

    def change_screen(self, screen_name):
        self.manager.transition = FadeTransition()
        self.manager.current = screen_name
