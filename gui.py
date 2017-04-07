from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import time
import polynanna
import webbrowser


class PolyNannaApp:

    def __init__(self, master):

        self.master = master

        self.master.title('PolyNanna')
        self.master.resizable(False, False)
        self.master.configure(background='#B2EDCE')

        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.file = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='About', command=self.open_readme)
        self.file.add_command(label='Quit', command=self._safe_close)
        self.options = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(menu=self.options, label='Options')
        self.options.add_command(label='', command=lambda: None)

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#B2EDCE', font=('Profont', 18))
        self.style.configure('TButton', background='#B2EDCE', font=('Profont', 18))
        self.style.configure('TLabel', background='#B2EDCE', font=('Profont', 12))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.tophat = PhotoImage(file='tophat.png')
        self.pyfile = PhotoImage(file='py.png')
        self.gift = PhotoImage(file='gift.png')
        self.tree = PhotoImage(file='tree.png')
        self.readme_text = 'Test Text'

        ttk.Label(self.frame_header, wraplength=245, text='POLYNANNA',  font=('Profont', 28)).grid(row = 0, column = 0, columnspan=4, sticky = 'n')
        ttk.Label(self.frame_header, image=self.tophat, background='#fc9f9f').grid(row=1, column=0)
        ttk.Label(self.frame_header, image=self.pyfile, background='#AFE0FF').grid(row=1, column=1)
        ttk.Label(self.frame_header, image=self.tree, background='#B2EDCE').grid(row=1, column=2)
        ttk.Label(self.frame_header, image=self.gift, background='#AFE0FF').grid(row=1, column=3)
        ttk.Label(self.frame_header, image=self.tophat, background='#fc9f9f').grid(row=2, column=1)
        ttk.Label(self.frame_header, image=self.pyfile, background='#AFE0FF').grid(row=2, column=2)
        ttk.Label(self.frame_header, image=self.tree, background='#B2EDCE').grid(row=2, column=3)
        ttk.Label(self.frame_header, image=self.gift, background='#AFE0FF').grid(row=2, column=0)
        ttk.Label(self.frame_header, image=self.tophat, background='#AFE0FF').grid(row=3, column=3)
        ttk.Label(self.frame_header, image=self.pyfile, background='#B2EDCE').grid(row=3, column=0)
        ttk.Label(self.frame_header, image=self.tree, background='#B2EDCE').grid(row=3, column=1)
        ttk.Label(self.frame_header, image=self.gift, background='#fc9f9f').grid(row=3, column=2)
        ttk.Label(self.frame_header, image=self.tophat, background='#fc9f9f').grid(row=4, column=0)
        ttk.Label(self.frame_header, image=self.pyfile, background='#AFE0FF').grid(row=4, column=1)
        ttk.Label(self.frame_header, image=self.tree, background='#B2EDCE').grid(row=4, column=2)
        ttk.Label(self.frame_header, image=self.gift, background='#AFE0FF').grid(row=4, column=3)
        ttk.Label(self.frame_header, wraplength = 245, text = self.readme_text).grid(row=5, column=0, columnspan=4, sticky='n')

        self.button_header = ttk.Frame(master)
        self.button_header.pack()
        ttk.Button(self.button_header, text='Run Drawing', command=self.run_drawing, width=20).grid(row=0, column=0)


    def run_drawing(self):
        start_time = time()
        polynanna.main()
        runtime = round((time() - start_time), 5)
        messagebox.showinfo(title='Success', message='You are awesome. Drawing completed in {} seconds.'.format(runtime))

    def open_readme(self):
        webbrowser.open('https://github.com/joemarchese/PolyNanna/blob/master/README.md')

    def _safe_close(self):
        self.master.destroy()


def main():

    root = Tk()
    app = PolyNannaApp(root)
    root.mainloop()

if __name__ == '__main__': main()
