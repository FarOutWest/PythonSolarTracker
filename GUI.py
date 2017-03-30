#! /usr/bin/env python3
from  tkinter import *

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

        chargeLabel = Label(self, text = "Total System Charge: ")
        chargeLabel.place(x = 10, y = 10)

        VinLabel = Label(self, text = "Solar Voltage Input: ")
        VinLabel.place(x = 10, y = 60)

        estimatedLabel = Label(self, text = "Estimated Total Run Time: ")
        estimatedLabel.place(x = 10, y = 110)

        menu = Menu(self.master)
        self.master.config(menu = menu)

        file = Menu(menu)
        #file.add_command(label = "Show Text", command = self.show_txt)
        file.add_command(label = "Exit", command = self.client_exit)
        menu.add_cascade(label = "File", menu = file)

        #other = Menu(menu)
        #other.add_command(label = "Other")
        #menu.add_cascade(label = "Item in Other", menu = other)

    def client_exit(self):
        exit()

    def start_tracking(self):
        exit()
        #call scripts to initialize tracking

    def stop_tracking(self):
        exit()
        #call scripts to terminate tracking

    #def show_txt(self):
        #text = Label(self, text = "SOME TEXT HERE")
        #text.pack()

root = Tk()
root.geometry("400x200")
app = Window(root)
root.mainloop()
