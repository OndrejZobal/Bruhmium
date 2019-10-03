import threading
import time
import queue

from Libraries import urllib3
from Libraries import tab

tabs = []   # List of open tabs. Only stores tab.Tab()
open_tab = 0   # An index of a tab inside tabs that is currently open
downloader_thread = None
drawer_thread = None
interrupt_draw = False
quitting = False
command_queue = queue.Queue()
default_url = 'http://www.seznam.cz'


def web_drawer(i):  # Draws the web onto the canvas
    global interrupt_draw
    global drawer_thread
    if interrupt_draw:
        return
    print(tabs[i].request.data)
    drawer_thread = None

def web_downloader(url):  # Downloads the web page and stores it
    http = urllib3.PoolManager()
    print(str(url))
    return http.request('GET', url)

def web_loader(url, create_new=True, draw=True):  # Downlands web and then draws it
    global open_tab
    if create_new:
        tabs.append(tab.Tab(url, web_downloader(url)))
    else:
        tabs[open_tab] = tab.Tab(url, web_downloader(url))
        open_tab = len(tabs) - 1
    if draw:
        draw_web(open_tab)
    print("Web Loaded")

''' 
These functions can be used to start processes, they basically just use the functions above, but they can set up important parameters and they 
launch the functions in their own threads. It is advised to use them instead of using the functions above directly.
'''

def draw_web(i=open_tab):
    global drawer_thread
    global interrupt_draw
    if drawer_thread is not None:
        interrupt_draw = True
        drawer_thread.join()
        interrupt_draw = False
    drawer_thread = threading.Thread(target=web_drawer, args=(i,))
    drawer_thread.start()

def load_web(url, create_new=True, draw=True):  # Starts Weabloader in a new thread
    #TODO clean this garbage.
    global downloader_thread
    downloader_thread = threading.Thread(target=web_loader, args=(url, create_new, draw))
    downloader_thread.start()

''''''


def command_manager():  # Takes cara of cli Commands. Runs in its own thread.
    print('CLI Manager Launched. Type "help" for help.')
    global open_tab
    global default_url
    global quitting
    while not quitting:
        try:
            while command_queue.empty():
                time.sleep(0.005)

            command = command_queue.get()

            if command[0] == 'quit':
                quitting = True
                print('Core is quitting. Press enter to finish')

            elif command[0] == 'help':
                print('Available commands:')
                print('opentab + url \n\tDownloads and draws a web-page in a brand new tab.')
                print('closetab + int \n\tCloses given tab.')
                print('loadpage + url \n\tDownloads and draws a web-page in a current tab.')
                print('changetab + int \n\tChanges the opened tab.')
                print('refresh\n\tRedownloads and redraws the current web-page.')
                print('tablist \n\tShows a list of all opened tabs.')
                print('quit \n\tQuits the Core threads.')

            elif command[0] == 'opentab':
                if len(command) > 1:
                    load_web(command[1])
                else:
                    print("Missing url")

            elif command[0] == 'loadpage':
                try:
                    if len(command) >= 1:
                        load_web(tabs[open_tab].urls[len(tabs[open_tab].urls) - 1], False)
                    else:
                        print("Missing url")
                except:
                    print('There has been a problem with your command')

            elif command[0] == 'changetab':
                try:
                    if len(command) > 1:
                        if len(tabs) > int(command[1]):
                            open_tab = int(command[1])
                            web_drawer(open_tab)
                        else:   print('Given number is higher than the number of tabs')
                    else:   print('This command requires <int> to be given as an argument')
                except:
                    print('There has been a problem with your command. Make sure that the given argument was of type <int>')

            elif command[0] == 'refresh':
                try:
                    load_web(tabs[int(open_tab)].urls[len(tabs[int(open_tab)].urls) - 1], False)
                except:
                    print('There has been a problem with your command')

            elif command[0] == 'closetab':
                try:
                    if len(command) > 1:
                        if len(tabs) > int(command[1]):
                            if open_tab == int(command[1]):
                                if open_tab is not 0:
                                    open_tab -= 1
                                    command_queue.put('refresh')
                            tabs.pop(int(command[1]))
                            if len(tabs) == 0:
                                load_web(default_url, True, True)
                        else:   print('Given number is higher than the number of tabs')
                    else:   print('This command requires <int> to be given as an argument')
                except:
                    print('There has been a problem with your command. Make sure that the given argument was of type <int>')

            elif command[0] == 'tablist':
                if len(tabs) >= 1:
                    print('Open Tabs (' + str(len(tabs)) + '): ')
                    for i in range(len(tabs)):
                        if i == open_tab:
                            print(">>>", end='') #why the fuck
                        print('\t' + tabs[i].title + '\t|\t' + tabs[i].urls[len(tabs[i].urls) - 1])
                else:
                    print('There are no open tabs.')
            else:
                print('Unknown command: "' + command[0] + '".')
        except:
            print("Command Manager ran into an error!")


def cli_input():
    while not quitting:
        command_queue.put(input().lower().split(' '))

def main():
    command_manager_thread = threading.Thread(target=command_manager)
    cli_input_thread = threading.Thread(target=cli_input)
    command_manager_thread.start()
    cli_input_thread.start()

    command_queue.put(['opentab',default_url])
    print('Bruhmium-Core module loaded')

def debug():
    main()


if __name__ == '__main__':
    print('THIS SCRIPT IS NOT TO BE RAN ALONE \nDo you wish to continue in debug mode?\n')
    if input("y/n>") in ['yes', 'y', '1', 'ano', 'a']:
        debug()
    input('Press enter key to continue...')
else:
    main()
