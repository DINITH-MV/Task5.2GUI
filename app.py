from tkinter import *
from gpiozero import PWMLED

RED_LED = PWMLED(14)
BLUE_LED = PWMLED(15)
GREEN_LED = PWMLED(18)

win = Tk()
win.geometry("500x430")
win.title("LED Brightness Control")

var_red = DoubleVar()
var_blue = DoubleVar()
var_green = DoubleVar()

# Function to update label
def selectionRed(val):
    selection = f"Red LED Brightness Level: {int(float(val) * 100)}%"
    labelRed.config(text=selection)
    RED_LED.value = float(val)  # PWM expects a float between 0.0 and 1.0
    
def selectionBlue(val):
    selection = f"Blue LED Brightness Level: {int(float(val) * 100)}%"
    labelBlue.config(text=selection)
    BLUE_LED.value = float(val)  # PWM expects a float between 0.0 and 1.0
    
def selectionGreen(val):
    selection = f"Green LED Brightness Level: {int(float(val) * 100)}%"
    labelGreen.config(text=selection)
    GREEN_LED.value = float(val)  # PWM expects a float between 0.0 and 1.0

# Create the scale (0.0 to 1.0 for PWM)
RedLEDscale = Scale(win, variable=var_red, from_=0.0, to=1.0, resolution=0.01,
              orient=HORIZONTAL, length=320, label="RED LED",
              command=selectionRed, font="Lato")
RedLEDscale.pack(pady=20)

BlueLEDscale = Scale(win, variable=var_blue, from_=0.0, to=1.0, resolution=0.01,
              orient=HORIZONTAL, length=320, label="BLUE LED",
              command=selectionBlue, font="Lato")
BlueLEDscale.pack(pady=20)

GreenLEDscale = Scale(win, variable=var_green, from_=0.0, to=1.0, resolution=0.01,
              orient=HORIZONTAL, length=320, label="GREEN LED",
              command=selectionGreen, font="Lato")
GreenLEDscale.pack(pady=20)

# Label to show brightness
labelRed = Label(win, font='Lato')
labelRed.pack()
labelBlue = Label(win, font='Lato')
labelBlue.pack()
labelGreen = Label(win, font='Lato')
labelGreen.pack()

# Run the GUI event loop
try:
    win.mainloop()
except KeyboardInterrupt:
    print("Program interrupted. Turning off LED.")
    RED_LED.value = 0
    BLUE_LED.value = 0
    GREEN_LED.value = 0
