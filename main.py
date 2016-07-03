'''
Importing Librarys required for use of unicornhat
    -unicornhat
    -time, to allow wait states
    -characterLibrary has characters created in a 8x8 matrix, will check message to make sure all characters available
'''

'''import unicornhat as UH
import time
import characterLibrary'''

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
    for char in msg:
        listMsg.append(char)
    return listMsg

def main():
    print(messageConvertToList("Hello i am john"))
    pass

main()