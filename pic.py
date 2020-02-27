from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty

class Menu(GridLayout):
    rv = ObjectProperty(None)

    def pass_text(instance, value):
        instance.ids.output.text = value



class PIC(App):

    def build(self):
        return Menu()



if __name__ == '__main__':
    PIC().run()
