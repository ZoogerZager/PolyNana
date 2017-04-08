from random import choice
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from polynanna import *
import webbrowser


class PolyNannaApp:

    def __init__(self, master):

        self.master = master

        self.master.title('PolyNanna')
        self.master.resizable(False, False)
        self.colors = dict(blue='#AFE0FF', red='#fc9f9f', green='#B2EDCE')
        self.master.configure(background=self.colors.get('green'))

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='About', command=self.open_readme)
        self.file.add_command(label='Quit', command=self._safe_close)
        self.options = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.options, label='Options')
        self.printboolean, self.writeboolean, self.printallpossible = (BooleanVar(), BooleanVar(), BooleanVar())
        self.options.add_checkbutton(label='Print Results', variable=self.printboolean)
        self.options.add_checkbutton(label='Write Results', variable=self.writeboolean)
        self.options.add_checkbutton(label='Print All Possible Recipients', variable=self.printallpossible)

        self.style = ttk.Style()
        self.style.configure('TFrame', background=self.colors.get('green'), font=('Profont', 18))
        self.style.configure('TButton', background=self.colors.get('green'), font=('Profont', 18))
        self.style.configure('TLabel', background=self.colors.get('green'), font=('Profont', 12))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.tophat = PhotoImage(file='icons/tophat.png')
        self.pyfile = PhotoImage(file='icons/py.png')
        self.gift = PhotoImage(file='icons/gift.png')
        self.tree = PhotoImage(file='icons/tree.png')
        self.icons = [self.tophat, self.pyfile, self.gift, self.tree]
        self.readme_text = 'Test Text'

        ttk.Label(self.frame_header, wraplength=245, text='POLYNANNA',  font=('Profont', 28)).grid(row = 0, column = 0, columnspan=4, sticky = 'n')

        for row in range(4):
            for column in range(4):
                ttk.Label(self.frame_header, image=choice(self.icons),
                background=choice(list(self.colors.values()))).grid(row=row, column=column)

        ttk.Label(self.frame_header, wraplength = 245, text = self.readme_text).grid(row=5, column=0, columnspan=4, sticky='n')

        self.button_header = ttk.Frame(master)
        self.button_header.pack()
        ttk.Button(self.button_header, text='Run Drawing', command=self.run_drawing, width=20).grid(row=0, column=0)

    def run_drawing(self):
        polyanna = Polyanna()
        polyanna._write = self.writeboolean.get()
        polyanna._print = self.printboolean.get()
        polyanna._print_all_recipients = self.printallpossible.get()
        polyanna.build_participants()
        polyanna.build_all_history()
        if polyanna.run_drawing_until_completed():
            results = Results(polyanna)
            if polyanna._print:
                results.print_results
            if polyanna._write:
                results.write_full_results()
                results.write_individual_results()
            if polyanna._print_all_recipients:
                polyanna.print_all_possible_recipients()
        print('Fail Count: ', polyanna.failcount)
        messagebox.showinfo(title='Success', message='Drawing Completed. You are awesome.')

    def open_readme(self):
        webbrowser.open('https://github.com/joemarchese/PolyNanna/blob/master/README.md')

    def _safe_close(self):
        self.master.destroy()


def main():

    root = Tk()
    app = PolyNannaApp(root)
    root.mainloop()

if __name__ == '__main__': main()
