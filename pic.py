from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout

class Menu(GridLayout):
    pass


class PIC(App):

    def build(self):
        return Menu()



if __name__ == '__main__':
    PIC().run()
