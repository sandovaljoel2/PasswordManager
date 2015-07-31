from Tkinter import *

class Welcome():

	def __init__(self,master):
		self.master=master
		self.master.geometry('450x500+100+200')
		self.master.title('Welcome')

		self.label1=Label(self.master,text='Welcome to PassMan')
		self.button1=Button(self.master,text='Login',command=self.gotoMainMenu)


		self.label1.pack()
		self.button1.pack()

	def gotoMainMenu(self):

		root2=Toplevel(self.master)
		myGUI=MainMenu(root2)

	def finish(self):
		self.master.destroy()

class MainMenu():

	def __init__(self,master):
		self.master=master
		self.master.geometry('450x500+100+200')
		self.master.title('Main Menu')

		self.label1=Label(self.master,text='Welcome to PassMan')
		self.button1=Button(self.master,text='Logout')

		self.label1.pack()
		self.button1.pack()		

def main():

	root=Tk()
	myGUIWelcome=Welcome(root)
	root.mainloop()

if __name__ == '__main__':
	main()