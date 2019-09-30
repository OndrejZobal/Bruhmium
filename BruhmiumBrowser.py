import tkinter as tk
import BruhmiumCore
from tkinter import messagebox

def main():
    pass


def debug():
    pass


if __name__ == '__main__':
    print('THIS SCRIPT IS NOT TO BE RAN ALONE \nDo you wish to continue in debug mode?\n')
    if input(">") in ['yes', 'y', '1']:
        debug()
    input('Press any key to continue...')
else:
    print('Bruhmium-Browser module loaded')

class Okno_uzivatel:
    # vlastnosti: Label info_uzivatel1, Entry uzivatel1, Label info_heslo1, Entry heslo1
    #             Label overeni_udaju,
    #             Label info_uzivatel2, Entry uzivatel2, Label info_heslo2, Entry heslo2
    #             Button overeni

    def __init__(self):
        self.inicializaceOkna()
        self.obsahOkna()
        self.zviditelneniOkna()

    def inicializaceOkna(self):
        self.okno = tk.Tk()  # vytvori­ objekt grafickeho okna
        self.okno.title("Overeni uzivatele")  # nastavi­ titulek
        self.okno.geometry("400x100+400+400")

    def obsahOkna(self):


        # Creating Menubar
        self.menubar = tk.Menu(self.okno)
        self.menubar.add_command(label="Home")
        # Adding File Menu and commands
        tabs = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Tabs', menu=tabs)
        tabs.add_command(label='Tab_1', command=None)
        tabs.add_command(label='Tab_2', command=None)
        tabs.add_command(label='Tab_3', command=None)

        self.menubar.add_command(label="Options")
        self.menubar.add_command(label = "Quit", command = quit)


        self.info_uzivatel1 = tk.Label(self.okno, text = "Uzivatel: ")
        self.info_uzivatel1.grid(row = 0, column = 0)

        self.uzivatel1_string = tk.StringVar()
        self.uzivatel1 = tk.Entry(self.okno, textvariable = self.uzivatel1_string)
        self.uzivatel1.focus_set()  # kurzor v poli
        self.uzivatel1.grid(row = 0, column = 1)

        self.info_heslo1 = tk.Label(self.okno, text="      Heslo: ")
        self.info_heslo1.grid(row=0, column=2)

        self.heslo1_string = tk.StringVar()
        self.heslo1 = tk.Entry(self.okno, textvariable=self.heslo1_string, show = "*")
        self.heslo1.focus_set()  # kurzor v poli
        self.heslo1.grid(row=0, column=3)


        tk.Label(self.okno, text = "Overeni udaju:", font = 14).grid(row = 1, columnspan=3, sticky = "W")


        self.overeni = tk.Button(self.okno, text="Overeni", command = self.stisk_tlacitka, bg = "blue", fg = "skyblue", padx=20, pady=10)
        self.overeni.grid(row=3, column=3)

    def stisk_tlacitka(self):
        if neco :
            tk.messagebox.showinfo("nazev okna", "text")
        else:
            tk.messagebox.showerror("nazev okna", "text")

    def zviditelneniOkna(self):
        self.okno.config(menu = self.menubar)
        self.okno.mainloop()

    def quit(self):
        self.okno.destroy()

Okno_uzivatel()

