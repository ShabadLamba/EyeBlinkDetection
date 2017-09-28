from Tkinter import *
# from Tkinter import ttk
import ttk
from PIL import Image, ImageTk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Home Automation using Eye Blink")
        myColor = '#444444'                 # Its a light blue color
        master.configure(bg=myColor)          # Setting color of main window to myColor
        
        topframe = Frame(master,bg=myColor)
        topframe.grid(row=0,)

        listOfDevicesframe = Frame(master,bg=myColor)
        listOfDevicesframe.grid(row=1,pady=20,sticky='w', padx=30)

        leftframe = Frame(master,bg=myColor)
        leftframe.grid(row=2,column=0,sticky='w',pady=10, padx=30 )

        labelframe = LabelFrame(root, text="", fg='#444444' ,bg=myColor)
        labelframe.grid(row=3,column=0,sticky='w',pady=40, padx=30)
 
        #top frame
        self.label = Label(topframe, text="HOME AUTOMATION USING EYE BLINK",fg='#FFFFFF',bg=myColor, font=("Courier", 28))
        self.label.pack(expand='YES',fill=None,padx=20)

        self.label = Label(listOfDevicesframe, text="LIST OF DEVICES",fg='#FFFFFF',bg=myColor,font=("Courier", 18))
        self.label.pack(side='left',expand='YES',fill=None)

        #left frame
        led_photo = PhotoImage(file="ledlightblue.gif")
        fan_photo = PhotoImage(file="3D_Blower_converted.gif")
        alarm_photo = PhotoImage(file="buzzer_converted.gif")

        self.button1 = Button(leftframe, text="Led1", command=self.led1, height=3, width=30, bg=myColor, compound=CENTER, fg='#666666',highlightcolor='black')
        self.button1.bind("<Enter>", lambda event, h=self.button1: h.configure(fg='black'))
        self.button1.bind("<Leave>", lambda event, h=self.button1: h.configure(fg='#666666'))

        self.button1.pack(pady=5,expand='YES',fill='both')

        self.button1.image = led_photo

        self.button2 = Button(leftframe, text="Led2", command=self.led2, height=3, width=30, bg=myColor, compound=CENTER, fg='#666666',highlightcolor='black')
        self.button2.bind("<Enter>", lambda event, h=self.button2: h.configure(fg='black'))
        self.button2.bind("<Leave>", lambda event, h=self.button2: h.configure(fg='#666666'))
        self.button2.pack(pady=5,expand='YES',fill='both')


        self.button3 = Button(leftframe, text="Led3", command=self.led3, height=3, width=30, bg=myColor, compound=CENTER, fg='#666666',highlightcolor='black')
        self.button3.bind("<Enter>", lambda event, h=self.button3: h.configure(fg='black'))
        self.button3.bind("<Leave>", lambda event, h=self.button3: h.configure(fg='#666666'))
        self.button3.pack(pady=5,expand='YES',fill='both')

        self.button4 = Button(leftframe, text="Fan", command=self.fan, height=3, width=30, bg=myColor, compound=CENTER, fg='#666666',highlightcolor='black')
        self.button4.bind("<Enter>", lambda event, h=self.button4: h.configure(fg='black'))
        self.button4.bind("<Leave>", lambda event, h=self.button4: h.configure(fg='#666666'))
        self.button4.pack(pady=5,expand='YES',fill='both')

        self.button4.image = fan_photo

        self.button5 = Button(leftframe, text="Alarm", command=self.alarm, height=3, width=30, bg=myColor, compound=CENTER, fg='#666666',highlightcolor='black')
        self.button5.bind("<Enter>", lambda event, h=self.button5: h.configure(fg='black'))
        self.button5.bind("<Leave>", lambda event, h=self.button5: h.configure(fg='#666666'))
        self.button5.pack(pady=5,expand='YES',fill='both')

        self.button5.image = alarm_photo

        #bottom frame
        self.label = Label(labelframe, text="INSTRUCTIONS\n To select any device blink your eyes \
x number of time and wait you t secs from next step.", fg='orange',bg=myColor)
        self.label.pack()

        # self.close_button = Button(bottomframe, text="Close", command=master.quit)
        # self.close_button.pack(side='left',expand='YES')

    def led1(self):
        print("LED 1")

    def led2(self):
        print("LED 2")

    def led3(self):
        print("LED 3")

    def fan(self):
        print("FAN")

    def alarm(self):
        print("ALARM")


root = Tk()
root.geometry("600x600+350+0")
my_gui = MyFirstGUI(root)
root.mainloop() 