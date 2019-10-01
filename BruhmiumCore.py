import threading
import time
from Libraries import requests
from Libraries import tab

tabs = []
openedtab = 0
downloader = None
clithread = None
quitting = False



def webdownlader(url):  # Downloads the webpage and stores it
    return requests.get(url=url)


def webdraw(i):  # Draws the web onto the canvas
    print(tabs[i].request.text)


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


def cli():
    global quitting
    while not quitting:
        command = input().lower().split(' ')
        if command[0] == 'quit':
            quitting = True
        elif command[0] == 'help':
            print('bruh')
        elif command[0] == 'loadpage':
            if len(command) > 1:
                loadweb(command[1])
            else:
                print("Missing url")


def main():
    global clithread
    clithread = threading.Thread(target=cli)
    clithread.start()
    print('CLI Manager Launched')


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
