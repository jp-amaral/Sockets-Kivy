from kivy.app import App
import math
import sys
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg

import matplotlib.pylab as plt
x= [1,2,3,4,5,6]
y=[1,2,3,4,5,6]

plt.plot(x,y)

plt.ylabel("Y axis")
plt.xlabel("X axis")
class CpuMem(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(plt.gof()))

class Main(App):
    def build(self):
        Builder.load_file("Layout_yt.kv")
        return CpuMem()

Main().run()
        

