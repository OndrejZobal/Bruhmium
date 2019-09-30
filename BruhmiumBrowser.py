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
        self.okno.geometry("1000x900+400+0")

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


        # URL-entry, back button

        self.ulrMenuFrame = tk.Frame()
        self.backButton = tk.Button(self.ulrMenuFrame, text = "<-")
        self.backButton.grid(column = 0, row = 0, ipadx = 20, padx = 20)

        self.urlField = tk.Entry(width = 80)
        self.urlField.grid(column = 1, row = 0)

        #tab menu

        OPTIONS = ["Placeholder1", "Placeholder2", "Placeholder3"]  #opened tabs
        self.openedTab = tk.StringVar(self.ulrMenuFrame)            #active tab
        self.openedTab.set(OPTIONS[0])                              #default tab
        self.tabMenu = tk.OptionMenu(self.ulrMenuFrame, self.openedTab, *OPTIONS)
        self.tabMenu.grid(column = 2, row = 0)
        self.openedTab.trace("w", self.changed)

        self.ulrMenuFrame.grid(column = 0, row = 0)

    def changed(self, *args):      #funkce co se zavolá pokaždé co se změní tab
        print("SUCCESS")



    def zviditelneniOkna(self):
        self.okno.config(menu = self.menubar)
        self.okno.mainloop()