from tkinter import *

class Application(Frame):
	def __init__(self,master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()
	def create_widgets(self):
		self.inst_lbl = Label(self, text = "Enter password for secret to longevity")
		self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
		
		self.pw_lbl = Label(self, text = "Password: ")
		self.pw_lbl.grid(row = 1, column = 0, sticky = W)
		
		self.pw_ent = Entry(self)
		self.pw_ent.grid(row = 1, column = 1, sticky = W)
		
		self.submit_bttn = Button(self, text = "submit", command = self.reveal)
		self.submit_bttn.grid(row = 2, column = 0, sticky = W)
		
		self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
		self.secret_txt.grid(row = 3, column = 0, columnspan = 2, sticky = W)
	def reveal(self):
		contents = self.pw_ent.get()
		
		if contents =="secret":
			message = "here's the secret to living to 100: drink tons"
		else:
			message = "ya, about your password, it was wrong. try again or die young"
			
		self.secret_txt.delete(0.0, END)
		self.secret_txt.insert(0.0, message)
		

root = Tk()
root.title("Longevity")
root.geometry("300x150")
root["bg"] = "#9cabc1"


app = Application(root)

root.mainloop()