from kivy3 import kivy

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from Kivy.uix.popup import Popup

class BoxLayoutApp(App):
    def build(self):
        return BoxLayout()

class CustomPopup(Popup):
    pass

class SampleBoxLayout(BoxLayout):
    checkbox_is_active = ObjectProperty(False)

    def checkbox_18_clicked(selfself,instance,value):
        if value is True:
            print("The person is onboard")
        else:
            print("The person is offboard")

    Officers = ObjectProperty(True)
    ClusterChiefs = ObjectProperty(True)
    Departments = ObjectProperty(True)


class SampleApp(App):
    def build(self):
        window.clearcolor=(1,1,1,1)
        return SampBoxLayout()

sample_app=SampleApp()
sample_app.run()