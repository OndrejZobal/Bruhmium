import threading
import time

from Libraries import urllib3
from Libraries import tab

tabs = []   # List of open tabs. Only stores tab.Tab()
openedtab = 0   # An index of a tab inside tabs that is currently open
downloader = None
quitting = False


def webdownlader(url):  # Downloads the webpage and stores it
    http = urllib3.PoolManager()
    print(str(url))
    return http.request('GET', url)

def webdrawer(i):  # Draws the web onto the canvas
    print(tabs[i].request.data)

def webloader(url, createnew=True, draw=True):  # Downlads web and then draws it
    global openedtab
    if createnew:
        tabs.append(tab.Tab(url, webdownlader(url)))
    else:
        tabs[openedtab] = tab.Tab(url, webdownlader(url))
        openedtab = len(tabs) - 1
    if draw:
        drawweb(openedtab)
    print("Web Loaded")

''' 
These functions can be used to start processes, they basically just use the functions above, but they can set up important parameters and they 
launch the functions in their own threads. It is advised to use them instead of using the functions above directly.
'''

def drawweb(i):
    threading.Thread(target=webdrawer, args=(i,)).start()

def loadweb(url, createnew=True, draw=True):  # Starts Weabloader in a new thread
    #TODO clean this garbage.
    global downloader
    downloader = threading.Thread(target=webloader, args=(url, createnew, draw))
    downloader.start()

''''''

def cli():  # Takes cara of cli Commands. Runs in its own thread.
    print(r'CLI Manager Launched. Type "help" for help.')
    global openedtab
    while True:
        command = input().lower().split(' ')
        print('nice')
        if command[0] == 'quit':
            quit()

        elif command[0] == 'help':
            print('Available commands:')
            print('loadpage + url \n\tDownloads and draws a web page.')
            print('tabs \n\tShows a list of all opened tabs')

        elif command[0] == 'opentab':
            if len(command) >= 1:
                loadweb(command[1])
            else:
                print("Missing url")

        elif command[0] == 'loadpage':
            try:
                if len(command) >= 1:
                    loadweb(tabs[openedtab].urls[len(tabs[openedtab].urls)-1], False)
                else:
                    print("Missing url")
            except:
                print('There has been a problem with your command')

        elif command[0] == 'changetab':
            try:
                if len(command) > 1:
                    if len(tabs) > int(command[1]):
                        openedtab = int(command[1])
                        webdrawer(openedtab)
            except:
                print('There has been a problem with your command')

        elif command[0] == 'refresh':
            try:
                loadweb(tabs[int(openedtab)].urls[len(tabs[int(openedtab)].urls)-1], False)
            except:
                print('There has been a problem with your command')

        elif command[0] == 'tablist':
            if len(tabs) >= 1:
                print('Open Tabs (' + str(len(tabs)) + '): ')
                for i in range(len(tabs)):
                    if i == openedtab:
                        print(">>>", end='') #why the fuck
                    print('\t' + tabs[i].title + '\t|\t' + tabs[i].urls[len(tabs[i].urls) - 1])
            else:
                print('There are no open tabs.')
        else:
            print('Unknown command: "' + command[0] + '".')


def main():
    threading.Thread(target=cli).start()


def debug():
    main()
    loadweb("http://wikipedia.org")
    loadweb("http://seznam.cz")
    loadweb("http://fb.com")


if __name__ == '__main__':
    print('THIS SCRIPT IS NOT TO BE RAN ALONE \nDo you wish to continue in debug mode?\n')
    if input(">") in ['yes', 'y', '1']:
        debug()
    input('Press enter key to continue...')
else:
    print('Bruhmium-Core module loaded')
    main()
