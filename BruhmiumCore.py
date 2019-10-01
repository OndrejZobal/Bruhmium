import threading
import time
#from Libraries import requests
from Libraries import urllib3
from Libraries import tab

tabs = []
openedtab = 0
downloader = None
clithread = None
quitting = False



def webdownlader(url):  # Downloads the webpage and stores it
    http = urllib3.PoolManager()
    return http.request('GET', url)


def webdraw(i):  # Draws the web onto the canvas
    print(tabs[i].request.data)


def webloader(url):  # Downlads web and then draws it
    global openedtab
    tabs.append(tab.Tab(url, webdownlader(url)))
    openedtab = len(tabs)-1
    webdraw(openedtab)
    print("Web Loaded")


def loadweb(url):  # Starts Weabloader in a new thread
    global downloader
    downloader = threading.Thread(target=webloader, args=(url,))
    downloader.start()


def cli():  # Takes cara of cli I/O. Runs in its own thread.
    global quitting
    while not quitting:
        command = input().lower().split(' ')
        if command[0] == 'quit':
            quit()
        elif command[0] == 'help':
            print('Available commands:')
            print('loadpage + url \n\tDownloads and draws a web page.')
            print('tabs \n\tShows a list of all opened tabs')
        elif command[0] == 'loadpage':
            if len(command) > 1:
                loadweb(command[1])
            else:
                print("Missing url")
        elif command[0] == 'tabs':
            if len(tabs) > 1:
                print('Open Tabs:')
                for i in tabs:
                    print('\t'+i.title+'\t>\t'+i.urls[len(i.urls)-1])
            else:
                print('There are no open tabs.')
        else:
            print('Unknown command: "'+command[0]+'".')


def main():
    global clithread
    clithread = threading.Thread(target=cli)
    clithread.start()
    print(r'CLI Manager Launched. Type "help" for help.')


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
