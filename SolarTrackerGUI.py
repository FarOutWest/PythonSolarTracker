import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import webbrowser

LARGE_FONT= ("Verdana", 12)

volts = 0
amps = 0
watts = volts * amps

class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Sunflower Solar Tracker")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, VoltPage, AmpPage, WattPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        startButton = ttk.Button(self, text = "Start", command = self.start_tracking)
        startButton.place(x = 135, y = 165)

        stopButton = ttk.Button(self, text = "Stop", command = self.stop_tracking)
        stopButton.place(x = 235, y = 165)

        gitHub = ttk.Button(self, text = "Visit GitHub Repository", command = self.open_GitHub)
        gitHub.place(x = 135, y = 215)

#NEEDS TO DYNAMICALLY UPDATE
        voltLabel = tk.Label(self, text = "Solar Cell Voltage: ")
        voltLabel.place(x = 10, y = 10)

        voltValue = tk.Label(self, text = "{} V".format(volts))
        voltValue.place(x = 220, y = 10)

        voltHistory = ttk.Button(self, text = "History", command = lambda: controller.show_frame(VoltPage))
        voltHistory.place(x = 350, y = 10)

#NEEDS TO DYNAMICALLY UPDATE
        ampLabel = tk.Label(self, text = "Solar Cell Amperage: ")
        ampLabel.place(x = 10, y = 60)

        ampValue = tk.Label(self, text = "{} A".format(amps))
        ampValue.place(x = 220, y = 60)

        ampHistory = ttk.Button(self, text = "History", command = lambda: controller.show_frame(AmpPage))
        ampHistory.place(x = 350, y = 60)

#NEEDS TO DYNAMICALLY UPDATE
        wattLabel = tk.Label(self, text = "System Wattage: ")
        wattLabel.place(x = 10, y = 110)

        wattValue = tk.Label(self, text = "{} W".format(watts))
        wattValue.place(x = 220, y = 110)

        wattHistory = ttk.Button(self, text = "History", command = lambda: controller.show_frame(WattPage))
        wattHistory.place(x = 350, y = 110)

    def start_tracking(self):
        #call scripts to initialize tracking
        print("START TRACKING")

    def stop_tracking(self):
        #call scripts to terminate tracking
        print("STOP TRACKING")

    def open_GitHub(self):
        webbrowser.open('https://github.com/FarOutWest/PythonSolarTracker', new=2)

class VoltPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Voltage History", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class AmpPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Amperage History", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class WattPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Wattage History", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(f, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

app = Window()
app.mainloop()
