# #This time, we aren't doing the star imports; instead, we'll keep
# Tkinter and the ttk objects in their own namespaces. This keeps
# our global namespace from being cluttered up and eliminates a
# potential source of bugs.

import tkinter as tk
from tkinter import ttk

# The Frame class is a generic
# Tk widget that is typically used as a container for other widgets. We
# can add any number of widgets to the Frame class, then treat the whole
# thing as though it were a single widget.
class HelloVeiw(tk.Frame):
    """A Friendly little module"""

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs) #The super() function gives us a
        # reference to the super class (the class we've subclassed, in this case,
        # tk.Frame). By calling the super class constructor and passing along *args
        # and **kwargs, our new HelloWidget class can take any arguments that Frame
        # can take.
        self.name = tk.StringVar()
        self.hello_string = tk.StringVar()
        self.hello_string.set("Hello World")#Tkinter variable requires use of
        # the set() method, rather than direct assignment. Likewise, retrieving
        # the data requires use of a get() method.

        name_label = ttk.Label(self, text="Name:")
        name_entry = ttk.Entry(self, textvariable=self.name) # By passing a Tkinter StringVar variable to this
        # argument, the contents of the Entry box will be bound to the variable,
        # and we can access it without needing to reference the widget.
        # Whenever a user enters text in the Entry object, self.name will
        # immediately be updated wherever it appears.

        ch_button = ttk.Button(self, text="Change",command=self.on_change) #command, which
        # takes a reference to a Python function or method. We call a function
        # or method passed this way a callback, and, as you might expect, this
        # callback will be called when the button is clicked. This is the simplest
        # way to bind functions to a widget

        hello_label = ttk.Label(self, textvariable=self.hello_string,font=("TkDefaultFont", 64), wraplength=600)
        #textvariable argument; on a label, the textvariable variable determines what will be displayed. By doing
        # this, we can change the text on the label by simply changing
        # self.hello_string. We'll also set a much larger font by using the font
        # argument, which takes a tuple in the format (font_name, font_size).
        #The wraplength argument specifies how wide the text can be before it
        # wraps to the next line.

        name_label.grid(row=0, column=0, sticky=tk.W)
        name_entry.grid(row=0, column=1, sticky=(tk.W + tk.E))
        ch_button.grid(row=0, column=2, sticky=tk.E)
        hello_label.grid(row=1, column=0, columnspan=3)
        #In this case, we're adding our widgets using the grid() geometry
        # manager, rather than the pack() geometry manager we used before. As
        # the name implies, grid() allows us to position widgets on their
        # parent object using rows and columns, much like a spreadsheet or
        # HTML table. Our first three widgets are arranged across three
        # columns in row 0, while hello_label will be on the second row (row 1).
        # The sticky argument takes a cardinal direction (N, S, E, or W—you can
        # either use strings or the Tkinter constants), which specifies which side
        # of the cell the contents must stick to. You can add these together to
        # stick the widget to multiple sides; for example, by sticking the
        # name_entry widget to both the east and west sides, it will stretch to fill
        # the whole width of the column. The grid() call for hello_label uses the
        # columnspan argument. As you might expect, this causes the widget to
        # span three grid columns. Since our first row established three columns
        # for the grid layout, we need to span all three if we want this widget to
        # fill the width of the application. Finally, we'll finish the __init__()
        # method by adjusting the grid configuration:

        self.columnconfigure(1, weight=1) #Here, we're telling it to weight
        # column 1 (the second column) more than the others. By doing this, the
        # second column of the grid (where our entry lives) will expand horizontally and
        # squash surrounding columns to their minimum widths. There is also a rowconfigure()
        # method for making similar changes to grid rows.

    def on_change(self):
        if self.name.get().strip():
            self.hello_string.set("Hello " + self.name.get())
        else:
            self.hello_string.set("Hello World")

        #To get the value of the text entry, we call the get() method of its
        # text variable. If this variable contains any characters (notice we
        # strip the white space), we'll set our hello text to greet the name
        # entered; otherwise, we'll just greet the whole world.

class MyApplication(tk.Tk):
    """Hello World Main Application

    This time, we subclass Tk, which will represent our main
    application object.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Hello Tkinter")
        self.geometry("800x600")
        self.resizable(width=True, height=True)


        HelloVeiw(self).grid(sticky=(tk.E + tk.W + tk.N + tk.S))
        self.columnconfigure(0, weight=1)


if __name__ == '__main__':
    app = MyApplication()
    app.mainloop()