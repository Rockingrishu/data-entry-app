from tkinter import *  #import tkinter in global namespace
from tkinter.ttk import * #This imports the ttk or themed Tk widget library.

#This creates our root or master application object. This represents the primary top-level window and main execution thread
#of the application, so there should be one and only one instance of Tk for every application.
root = Tk()

#This creates a new Label object. As the name implies, a Label object is just a widget for displaying
#text (or images).
label = Label(root,text="Hello world")
button = Button(root,text=" click me.") #create a clickable button.
entry = Entry(root,text="Fill me world") # create a entry feild.

entry.pack() #this places the new button widget onto its parent widget.
button.pack()# this places the new entry widget onto its parent widget.
label.pack() #This places the new label widget onto its parent widget.
root.mainloop() #This final line starts our main event loop. This loop
# is responsible for processing all the events—keystrokes, mouse clicks, and so on—and it will run until the program is quit.


