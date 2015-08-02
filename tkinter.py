import Tkinter as ttk


LARGE_FONT= ("Verdana", 12)


class PasswordApplication(ttk.Tk):

    def __init__(self, *args, **kwargs):
        
        ttk.Tk.__init__(self, *args, **kwargs)
        ttk.Tk.wm_title(self, "Password Manager")
        container = ttk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, MainMenu, NewLogin):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Welcome to Password Manager", font=LARGE_FONT)
        label.pack(pady=5,padx=100)
        label1 = ttk.Label(self, text="Enter your Password to Login", font=LARGE_FONT)
        label1.pack(pady=0,padx=10)

        entry = ttk.Entry(self)
        entry.config(show='*')
        entry.pack()

        button = ttk.Button(self, text="Login",
                            command=lambda: controller.show_frame(MainMenu))
        button.pack()

        button2 = ttk.Button(self, text="Exit",
                            command=lambda: controller.destroy())
        button2.pack()


class MainMenu(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="Add New Login",
                            command=lambda: controller.show_frame(NewLogin))
        button2.pack()



def generate_pass(length, special):
    print length.get()
    print special.get()

class NewLogin(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Add New Login!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        label1 = ttk.Label(self, text="Name")
        label1.pack()

        E1 = ttk.Entry(self)
        E1.pack()

        label2 = ttk.Label(self, text="User ID")
        label2.pack()

        E2 = ttk.Entry(self)
        E2.pack()

        label3 = ttk.Label( self, text="Password")
        label3.pack()

        E3 = ttk.Entry(self)
        E3.pack()

        label4 = ttk.Label( self, text="Length")
        label4.pack()

        scale = ttk.Scale(self, from_=8, to=100)
        scale.config(orient=ttk.HORIZONTAL)
        scale.pack()

        label5 = ttk.Label(self, text="Special Characters")
        label5.pack()


        var = ttk.IntVar()

        E5 = ttk.Checkbutton(self, text="Yes", \
                 onvalue = 1, offvalue = 0, variable=var)
        E5.pack()

        generate = ttk.Button(self, text = "Generate Password", command = lambda: generate_pass(scale, var))
        generate.pack()


        submit = ttk.Button(self, text ="Save")
        submit.pack()

        button2 = ttk.Button(self, text="Main Menu",
                            command=lambda: controller.show_frame(MainMenu))
        button2.pack()


app = PasswordApplication()
app.mainloop()