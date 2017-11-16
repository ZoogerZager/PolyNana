from random import choice
from tkinter import *
from tkinter import ttk
import run_drawing
import webbrowser


class PolyNannaApp:

    def __init__(self, master):

        self.master = master
        self.master.title('PolyNanna')
        self.master.resizable(False, False)
        self.colors = dict(blue='#AFE0FF', red='#fc9f9f', green='#B2EDCE')
        self.master.configure(background=self.colors.get('green'))

        # Configure The Menu
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='About', command=self.open_readme)
        self.file.add_command(label='Quit', command=self._safe_close)

        # Set the Styles
        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.colors.get('green'), font=('Profont', 18))
        self.style.configure('TButton', background=self.colors.get('green'), font=('Profont', 24))
        self.style.configure('TLabel', background=self.colors.get('green'), font=('Profont', 11))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.tophat = PhotoImage(file='static/tophat.png')
        self.pyfile = PhotoImage(file='static/py.png')
        self.gift = PhotoImage(file='static/gift.png')
        self.tree = PhotoImage(file='static/tree.png')
        self.icons = [self.tophat, self.pyfile, self.gift, self.tree]

        for row in range(4):
            for column in range(4):
                ttk.Label(self.frame_header, image=choice(self.icons),
                background=choice(list(self.colors.values()))).grid(row=row, column=column)

        ttk.Label(self.frame_header, wraplength=500, text='POLYNANNA', font=('Profont', 50)).grid(row=4, column=0, columnspan=4, sticky='n')

        self.button_header = ttk.Frame(master)
        self.button_header.pack()
        ttk.Button(self.button_header, text='Run Drawing', command=self.run_polynanna_drawing, width=23).grid(row=0, column=0)

    def run_polynanna_drawing(self):
        run_drawing.main()

    def open_readme(self):
        webbrowser.open('https://github.com/joemarchese/PolyNanna/blob/master/README.md')

    def _safe_close(self):
        self.master.destroy()


def main():

    root = Tk()
    app = PolyNannaApp(root)
    root.mainloop()

if __name__ == '__main__': main()
