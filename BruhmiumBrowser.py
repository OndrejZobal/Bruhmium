import tkinter
import BruhmiumCore


# Defining a whole bunch of variables for Tkinter elements
tabs = back_button = search_entry = menu_bar = window = upper_menu_frame = search_button = \
    open_tab_stringvar = None


def window_initialization():    # Creates the window and all the elements, then it locks the main thread inside a loop.
    global tabs, window, menu_bar, back_button, upper_menu_frame, search_entry, search_button, open_tab_stringvar

    # Sets up window's attributes
    window = tkinter.Tk()
    window.title('Bruhmium Bruser')
    window.geometry('1000x900+400+0')

    # Creating the cool bar on the top (menu_bar)
    menu_bar = tkinter.Menu(window)
    menu_bar.add_command(label='Home')
    menu_bar.add_command(label='Options')
    menu_bar.add_command(label='Quit', command=BruhmiumCore.quit_bruhmium)

    # Creating a upper_menu_frame - a frame that contains all elements above canvas
    upper_menu_frame = tkinter.Frame(window)
    upper_menu_frame.grid(row=0, column=0)

    # Creating back_button - a button to load the previous address
    back_button = tkinter.Button(upper_menu_frame, text='Back')
    back_button.grid(column=0, row=0, ipadx=20, padx=20)

    # Creating search_entry - an input field to enter the web address
    search_entry = tkinter.Entry(upper_menu_frame, width=80)
    search_entry.grid(column=2, row=0)

    # Creating open_tab_stringvar - a stringvar containing information about currently opened tab
    open_tab_stringvar = tkinter.StringVar(upper_menu_frame)

    # Creating search_button - loads page on the address int the search_entry
    search_button = tkinter.Button(upper_menu_frame, text='Search', command=search)
    search_button.grid(row=0, column=3)

    # This is where the shit gets real
    window.config(menu=menu_bar)
    tab_selector_refresh()
    window.mainloop()


def change_tab(*args):
    print('Tab was changed successfully (' + str(args) + ').')


def tab_selector_refresh():
    global menu_bar
    '''
    try:
        menu_bar.destroy()

    except:
        pass
    '''
    opened_tab = tkinter.StringVar(upper_menu_frame)
    tab_selector_menu = tkinter.OptionMenu(upper_menu_frame, opened_tab, [])

    tab_selector_menu.grid(column=1, row=0)
    opened_tab.trace('w', change_tab)


def search():
    pass


def core_link():    # An important function that sets some Core variables to corresponding functions, also starts core
    BruhmiumCore.ui_refresh = tab_selector_refresh

    BruhmiumCore.main()


def main():
    print('Bruhmium-Browser module loaded')
    core_link()
    window_initialization()


def debug():    # Gets executed when executing the file directly. No one ever uses it
    main()


if __name__ == '__main__':  # This goes last
    print('THIS SCRIPT IS NOT TO BE RAN ALONE \nDo you wish to continue in debug mode?\n')
    if input("y/n>") in ['yes', 'y', '1', 'ano', 'a', 'jo', 'j']:
        debug()
    input('Press any key to continue...')
