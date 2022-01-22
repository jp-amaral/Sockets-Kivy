import pandas as pd
from matplotlib import pyplot as plt
import random
# import kivy module
from cv2 import exp
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.cache import Cache
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
graph1 = Image(source='graph1.png')
graph2 = Image(source='graph2.png')

class Calculator(App):
    def build(self):
        #image
        global graph1
        global graph2
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')
        VB = GridLayout()
        VB.cols = 1
        self.btn = Button(text="refresh",size_hint = (0.2,0.2),bold = True,background_color = "#00FFCE")
        self.btn.bind(on_press=self.callback)
        VB.add_widget(self.btn)
        HB.add_widget(graph1)
        HB.add_widget(graph2)
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        print(graph1)
        print(graph2)
        return superBox
    def callback(self,instance):
        global graph1
        global graph2
        print("START")
        cpuinfo = random.randrange(1,100)
        x = [cpuinfo,100-cpuinfo]
        y = ["CPU in use","CPU free"]
        plt.pie(x,labels=y)
        plt.savefig("graph1")
        plt.close()
        meminfo = random.randrange(1,100)
        x = [meminfo,100-meminfo]
        y = ["MEM in use","MEM free"]
        plt.pie(x,labels=y)
        plt.savefig("graph2")
        plt.close()
        graph1 = Image(source='graph1.png')
        graph2 = Image(source='graph2.png')
        print("DO IT")
        self.refresh()

Calculator().run()