from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

class Menu(GridLayout):
    def on_enter(self, instance):
        print('===========================')


class PIC(App):

    def build(self):
        return Menu()



if __name__ == '__main__':
    PIC().run()
