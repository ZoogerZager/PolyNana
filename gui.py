from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from time import time
import polynanna

class PolyNannaApp:

    def __init__(self, master):

        master.title('PolyNanna')
        master.resizable(False, False)
        master.configure(background='#B2EDCE')

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#B2EDCE')
        self.style.configure('TButton', background='#B2EDCE', font=('Profont', 18))
        self.style.configure('TLabel', background='#B2EDCE', font=('Profont', 12))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.tophat = PhotoImage(file='tophat.png')
        self.pyfile = PhotoImage(file='py.png')
        self.gift = PhotoImage(file='gift.png')
        self.tree = PhotoImage(file='tree.png')
        self.readme_text = 'Test Text'

        ttk.Label(self.frame_header, wraplength=245, text='PolyNanna Drawing',  font=('Profont', 18)).grid(row = 0, column = 0, columnspan=4, sticky = 'n')
        ttk.Label(self.frame_header, image=self.tophat, background='#fc9f9f').grid(row=1, column=0)
        ttk.Label(self.frame_header, image=self.pyfile, background='#AFE0FF').grid(row=1, column=1)
        ttk.Label(self.frame_header, image=self.tree, background='#B2EDCE').grid(row=1, column=2)
        ttk.Label(self.frame_header, image=self.gift, background='#AFE0FF').grid(row=1, column=3)
        ttk.Label(self.frame_header, wraplength = 245, text = self.readme_text).grid(row=2, column=0, columnspan=4, sticky='n')

        self.button_header = ttk.Frame(master)
        self.button_header.pack()

        ttk.Button(self.button_header, text='Run Drawing', command=self.run_drawing, width=20).grid(row=0, column=0)


    def run_drawing(self):
        start_time = time()
        polynanna.main()
        runtime = round((time() - start_time), 5)
        messagebox.showinfo(title = 'Success', message = 'You are awesome. Drawing completed in {} seconds.'.format(runtime))


def main():

    root = Tk()
    app = PolyNannaApp(root)
    root.mainloop()

if __name__ == '__main__': main()
