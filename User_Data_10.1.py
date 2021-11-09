import os


#create a new directory
def createDirectory():
    userDirName = input ('What is the directory you would like this saved in?  ')
    dirc = os.path.join('C:\\Users\\18566\\Desktop\\python_work\\project\\', userDirName )
    try:
        if not os.path.exists(dirc):
         os.makedirs(dirc)
        return dirc
    except OSError:
        print('Error: Creating directory. '+ dirc)
    return dirc


#create file
def createFile():
    folder = os.path.join('/Users/18566/Desktop/python_work/project/', f'{folder_name}')
    userFileName = input ('What would like to name this info file? ')
    userName = 'John Smith'
    userAddress = '2501 rt 130 cinnaminson, NJ'
    userPhoneNumber = '1234567890'
    file_name = f'{userFileName}.txt'.format(folder_name)
    file = os.path.join(folder, file_name)
    f = open(file, 'w')
    f.write(f'\n{userName}')
    f.write(f'\n{userAddress}')
    f.write(f'\n{userPhoneNumber}')
    print ('\n\nText named "{}" was written to a file. Check your directory: {}'.format(file_name, folder))
    return file

def appendInfo():
    userName = 'Barry Johnson'
    userAddress = '55 S Street'
    userPhoneNumber = '5555555555'
    f = open(filepath, 'a')
    f.write(f'\n\n{userName}')
    f.write(f'\n{userAddress}')
    f.write(f'\n{userPhoneNumber}')

#open created text
def openInfoText():

    f = open(f'{filepath}', 'r')
    print (f.read())


dirCreateLoop = True
while dirCreateLoop == True:
    dirCreateInput = input ('Would you like to create a directory? "yes/no": ')
    if dirCreateInput == 'yes':
        folder_name = createDirectory()
        fileCreateLoop = False
        break
    elif dirCreateInput == 'no':
        print ('Goodbye!')
        fileCreateLoop = False
    else:
        print('Not a valid input.')

fileCreateLoop = True
while fileCreateLoop == True:
    fileCreateInput = input ('Would you like to create a file? "yes/no": ')
    if fileCreateInput == 'yes':
        filepath = createFile()
        fileCreateLoop = False
    elif fileCreateInput == 'no':
        fileCreateLoop = False
    else:
        print ('Not a valid input.')

appendCreateLoop = True
while appendCreateLoop == True:
    fileAppendInput = input ('Would you like to add more information to your file? "yes/no": ')
    if fileAppendInput =='yes':
        appendInfo ()
        appendCreateLoop = False
    elif fileAppendInput == 'no':
        appendCreateLoop = False
    else:
        print ('Not a valid input.')


openInfoText()
