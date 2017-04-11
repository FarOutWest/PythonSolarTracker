#! /usr/bin/env python3
from  tkinter import *
import webbrowser
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM) #set to Broadcom Control pin 18 is physical pin 12
gpio.setup(18, gpio.OUT) #set pin 18 to output
pwm = gpio.PWM(18, 100) #set pin 18 to PWM
pwm.start(5) #

amps = 0.0
volts = 0.0
watts = amps * volts

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        self.master.title("Sunflower Solar Tracker")
        self.pack(fill = BOTH, expand = 1)

        startButton = Button(self, text = "Start", command = self.start_tracking)
        startButton.place(x = 50, y = 165)

        stopButton = Button(self, text = "Stop", command = self.stop_tracking)
        stopButton.place(x = 275, y = 165)

        voltLabel = Label(self, text = "Solar Cell Voltage: ")
        voltLabel.place(x = 10, y = 10)

    #NEEDS TO DYNAMICALLY UPDATE
        voltValue = Label(self, text = "{} V".format(volts))
        voltValue.place(x = 200, y = 10)

        ampLabel = Label(self, text = "Solar Cell Amperage: ")
        ampLabel.place(x = 10, y = 60)

    #NEEDS TO DYNAMICALLY UPDATE
        ampValue = Label(self, text = "{} A".format(amps))
        ampValue.place(x = 200, y = 60)

    #NEEDS TO DYNAMICALLY UPDATE
        wattLabel = Label(self, text = "System Wattage: ")
        wattLabel.place(x = 10, y = 110)

        wattValue = Label(self, text = "{} W".format(watts))
        wattValue.place(x = 200, y = 110)

        menu = Menu(self.master)
        self.master.config(menu = menu)

        settings = Menu(menu)
        settings.add_command(label = "Open at Login", command = self.open_at_login)
        settings.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "Settings", menu = settings)

        help = Menu(menu)
        help.add_command(label = "GitHub Page", command = self.open_GitHub)
        menu.add_cascade(label = "Help", menu = help)

    def client_exit(self):
        exit()

    def open_at_login(self):
        #add code to open at login of System
        print("OPEN AT LOGIN")

    def start_tracking(self):
        #call scripts to initialize tracking
        print("START TRACKING")

    def stop_tracking(self):
        #call scripts to terminate tracking
        print("STOP TRACKING")

    def open_GitHub(self):
        #open the github repo page
        webbrowser.open('https://github.com/FarOutWest/PythonSolarTracker', new=2)

root = Tk()
root.geometry("400x200")
app = Window(root)
root.mainloop()
