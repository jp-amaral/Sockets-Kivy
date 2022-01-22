import pandas as pd
from matplotlib import pyplot as plt
import random
# import kivy module
from cv2 import exp
import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
class Calculator(App):
    def build(self):
        #image
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')
        self.graph1 = Image(source='graph1.png')
        self.graph2 = Image(source='graph2.png')
        VB = GridLayout()
        VB.cols = 1
        self.btn = Button(text="refresh",size_hint = (0.2,0.2),bold = True,background_color = "#00FFCE")
        self.btn.bind(on_press=self.callback)
        VB.add_widget(self.btn)
        HB.add_widget(self.graph2)
        HB.add_widget(self.graph1)
        superBox.add_widget(HB)
        superBox.add_widget(VB)
        return superBox
    def callback(self,instance):
        print("ok")
        cpuinfo = random.randrange(1,100)
        x = [cpuinfo,100-cpuinfo]
        y = ["CPU in use","CPU free"]
        plt.pie(x,labels=y)
        plt.savefig('graph1')
        plt.close()

        meminfo = random.randrange(1,100)
        x = [meminfo,100-meminfo]
        y = ["MEM in use","MEM free"]
        plt.pie(x,labels=y)
        plt.savefig("graph2")
        plt.close()
        self.graph1.source = 'graph1.png'
        self.graph2.source = 'graph2.png'
        self.graph2.reload()
        self.graph1.reload()

Calculator().run()