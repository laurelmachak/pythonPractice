from tkinter import *
#root widget is a window with a title bar and other decor provided by window manager.
#has to be created before any other widgets and there can only be 1 widget
root = Tk() 
#the Label Widget. Child of the root widget: (labels can contain text & images)
snake = PhotoImage(file="~/Pictures/snake.gif")

someWords = """i hope jpg works, if it doesnt
then oh well. Apparently only GIF & PPM/PGM
on their own, but an interface exists to
allow additional image file formats to be
added easily"""
w = Label(root, compound = LEFT,padx=10, text = someWords, image = snake).pack(side="right")
#fits size of window to the given text:
#w.pack()

#window won't appear 'til we enter the Tkinter event loop:
root.mainloop()