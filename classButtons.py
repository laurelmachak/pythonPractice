from tkinter import *

class Application(Frame):
    """ A GUI application that counts button clicks """
    def __init__(self, master):
        """ Initialize the Frame """
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()
    def create_widgets(self):
        """ Create a button that displays num of clicks """
        self.bttn = Button(self,)
        self.bttn["text"] = "Total Clicks: 0"
        self.bttn["command"] = self.update_count
        self.bttn.grid()
    def update_count(self):
        """ increase click count and display new total """
        self.bttn_clicks += 1
        self.bttn["text"] = "Total Clicks: " + str(self.bttn_clicks)
        
        

root = Tk()
root.title("I'm lazy and proud")
root.geometry("200x200")

app = Application(root)

root.mainloop()
