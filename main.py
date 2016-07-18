'''
Importing Librarys required for use of unicornhat
    -unicornhat
    -time, to allow wait states
    -characterLibrary has characters created in a 8x8 matrix, will check message to make sure all characters available
'''

#import unicornhat as UH
import time
import characterLibrary as cL
import sys

def userInput():
    '''
    Simple userInput function to keep the design simple on the console
    '''
    Message = str(input("\nInput: "))
    return  Message

def messageConvertToList(msg):
    '''
    Converts a string to a list
    :param msg: string message
    :return: list with all characters including whitespace
    '''
    listMsg = []
    for char in msg.upper():
        listMsg.append(char)
    return listMsg

def characterConverter(listMsg):
    pass

def main():
    print(characterConverter(messageConvertToList("Hi")))
    pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        #add interface to allow command line options ot be added
        main()