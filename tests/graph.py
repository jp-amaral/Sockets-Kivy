import socket, sys, psutil, random, kivy
import pandas as pd
from matplotlib import pyplot as plt

# import kivy module

kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.image import Image
from kivy.core.image import Image as CoreImage
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock


Window.size = (800, 600)

ip_addr = "127.0.0.1"
tcp_port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((ip_addr, tcp_port))

class Graph(App):
    def build(self):
        #image
        superBox = BoxLayout(orientation ='vertical')
        HB = BoxLayout(orientation ='horizontal')
        self.graph1 = Image(source='graph1.png')
        self.graph2 = Image(source='graph2.png')
        VB = GridLayout()
        VB.cols = 1
        self.btn = Button(text="Send info",size_hint = (0.2,0.2),bold = True,background_color = "#00FFCE")
        self.btn.bind(on_press=self.sendInfo)
        VB.add_widget(self.btn)
        HB.add_widget(self.graph2)
        HB.add_widget(self.graph1)
        superBox.add_widget(HB)
        superBox.add_widget(VB) 

        Clock.schedule_interval(self.update, 0.1)
        
        return superBox

    def update(self, *args):
        #Generating info
        cpuinfo = psutil.cpu_percent()
    
        #Saving CPU info
        x = [cpuinfo,100-cpuinfo]
        y = ["CPU in use","CPU free"]
        plt.pie(x,labels=y, shadow=True, autopct='%1.1f%%')
        plt.savefig('graph1')
        plt.close()

        #Saving memory info
        meminfo = psutil.virtual_memory().percent

        x = [meminfo,100-meminfo]
        y = ["MEM in use","MEM free"]
        plt.pie(x,labels=y, shadow=True, autopct='%1.1f%%')
        plt.savefig("graph2")
        plt.close()

        #Opening new graphs, reloading page
        self.graph1.source = 'graph1.png'
        self.graph2.source = 'graph2.png'
        self.graph2.reload()
        self.graph1.reload()
        Window.size = (800, 600)


    def sendInfo(self,instance):
        try:
            print("Sending info...")
            data = str(psutil.cpu_percent()) + "|" + str(psutil.virtual_memory().percent)
            sock.send(data.encode())
            print("Sent")
            response = sock.recv(1024).decode()
            print('Server response: {}'.format(response))
        except (socket.timeout, socket.error):
            print('Server error. Done!')
            sys.exit(0)

Graph().run()