from tkinter import *
import os
from tkinter.ttk import Combobox
from tkinter import messagebox

class File_handler:
    def __init__(self, main_folder):
        self.main_folder = main_folder

    def open_python(self, lang):
        python_file_list = os.listdir(self.main_folder + "/" + lang)
        return python_file_list
fh = File_handler("Notes")


class Gui(Tk):
    def __init__(self):
        # Initialising super class
        super().__init__()

        # Def diff parameters of Window title, size, bg etc
        self.main_frame = Frame(self, width=500, height=500)
        self.title("Notes")
        self.geometry("500x500")
        self.resizable(False, False)
        # self.photo = PhotoImage(file="Untitled.png")
        self.photo = PhotoImage(file="lib.png",width=500,height=500)

    def main_win(self):
        """
        Creating main window as soon as app opens user will see this window
        :return:
        """
        self.main_frame.place(x=0, y=0)

        self.frame = Label(self.main_frame, image=self.photo)
        self.frame.place(x=-2, y=0)

        head = Label(self.main_frame, text="Programmer's Library", bg="Black", fg="#ff4747",
                 font=("forte", 28, "bold"))#colour reddish #ff4747
        head.place(x=80, y=66)

        l1 = Label(self.main_frame, text="Choose a Language ", font=("comicsansms", 24, "italic", "bold"), bg="black",
                   fg="#cc9a86")
        l1.place(x=100, y=135)


        # Buttons for main window in color you can use hex rgb and name of color

        pyt = Button(self.main_frame, text="Python", font=("comicsansms", 12, "italic", "bold"), bg="green",
                     fg="white",
                     width=15, command=lambda: sec("python"))
        pyt.place(x=170, y=230)

        java = Button(self.main_frame, text="Java", font=("comicsansms", 12, "italic", "bold"), bg="green", width=15,
                      fg="white", command=lambda: sec("java"))
        java.place(x=170, y=280)

        cpp = Button(self.main_frame, text="C/C++", font=("comicsansms", 12, "italic", "bold"), bg="green", width=15,
                     fg="white", command=lambda: sec("c++"))
        cpp.place(x=170, y=330)

        html = Button(self.main_frame, text="HTML", font=("comicsansms", 12, "italic", "bold"), bg="green", width=15,
                      fg="white", command=lambda: sec("HTML"))
        html.place(x=170, y=380)

    def pyt_tab(self, lang):
        """
        Second Win for choosing topic of notes
        :param lang:
        :return:
        """
        win = Frame(self, width=500, height=500)
        win.place(x=0, y=0)
        self.title(lang)

        
        self.frame = Label(win, image=self.photo)
        self.frame.place(x=-2, y=0)

        title = Label(win, text=f"Welcome to {lang}", font=("forte", 26, "bold"), bg="black", fg="#ff4747")
        title.place(x=100, y=65)
       


        l1 = Label(win, text="Select a topic", font=("comicsansms", 22, "bold", "italic"), bg="black", fg="white")
        l1.place(x=150, y=150)

        operation = fh.open_python(lang)

        
        def select():
            file = opt.get() 
            Gui.read_value("Python.txt")
            

       
        opt = StringVar()
        box1 = Combobox(win, textvariable=opt, value=operation, width=15, font=("comicsansms", 13, "italic"))
        box1.place(x=170, y=200)

        def back():
            win.destroy()
            main()

        def ex():
            answer = messagebox.askyesno("Exit", "Do you really want to exit")
            if answer:
                win.destroy()

        b1 = Button(win, text="Select", font=("comicsansms", 16, "bold", "italic"), bg="green", fg="white", command=select)
        b1.place(x=210, y=330)
        b2 = Button(win, text="Back", font=("comicsansms", 16, "bold", "italic"), bg="green", fg="white", command=back)
        b2.place(x=110, y=380)
        b3 = Button(win, text="Exit", font=("comicsansms", 16, "bold", "italic"), bg="green", fg="white", command=ex)
        b3.place(x=320, y=380)
        mainloop()

    @staticmethod
    def read_value(file):
        """
        Reads the file content and shows to user as textview
        :param file:
        :return:
        """

        with open(file, "r", encoding="utf8") as f:
            data = f.read()
        w = Tk()
        w.title("Python")
        w.geometry("900x555")
        w.minsize(900, 555)
        w.maxsize(900, 555)
        w.configure(bg="black")

        scrollbar = Scrollbar(w, orient=VERTICAL)
        scrollbar.pack(side=RIGHT, fill=Y)

        t1 = Text(w, wrap=WORD, yscrollcommand=scrollbar.set, font=("comicsansms", 12),
                  bg="white")
        t1.pack(expand=TRUE, fill=BOTH)
        t1.insert(INSERT, data)
        t1.config(state=DISABLED)

        scrollbar.config(command=t1.yview)


a = Gui()


def main():
    a.main_win()


def sec(lang):
    a.main_frame.place(x=500, y=500)
    a.pyt_tab(lang)


main()
a.mainloop()
