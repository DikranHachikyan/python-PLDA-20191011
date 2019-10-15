#!/home/wizard/anaconda3/bin/python

def newFile():
    print('Create new file')

def saveFile():
    print('Save file')

def openFile():
    print('Open file')

def quitApp():
    print('Quit app')
    quit()

if __name__ == '__main__':
    action = {
          'n':newFile
        , 'o':openFile
        , 's':saveFile
        , 'q':quitApp
    }

    ch = input('Command [n-new,o-open,s-save,q-quit]:')

    if ch in action:
        action[ch]()
    else:
        print(f'Invalid Command:{ch}')