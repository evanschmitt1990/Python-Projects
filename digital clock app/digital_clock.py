from tkinter import Label, Tk
import time

# the specs for the clock, including the name
app_window = Tk()
app_window.title("Evan's Blue Clock")
app_window.geometry("420x120")
app_window.resizable(1,1)

# where the color and font are defined for the clock
text_font = ("Helvetica", 60, 'bold')
background = "blue"
foreground = "white"
border_width = 20

label = Label(app_window, font = text_font, bg = background, fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

# the function for the clock is defined below
def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

# this is where we run the app

digital_clock()
app_window.mainloop()
