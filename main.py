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
    '''
    Converts the list message to a list of co-ordinates [x,y] with the appropriate spacing between letters

    :param listMsg: Message to be converted
    :return: converted Message in [X,Y] with appropriate spacing
    '''
    convertedMsg = []
    spacing = 0
    for char in listMsg:
        tempCoOrd = []
        for CoOrds in cL.updatedCharDict[char]['Properties']['CoOrd']:
            CoOrds[0] += spacing
            tempCoOrd.append((CoOrds))

        convertedMsg.append(tempCoOrd)

        spacing += cL.updatedCharDict[char]['Properties']['CharLength']

    return convertedMsg

def main():
    print(characterConverter(messageConvertToList("Hi")))
    pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        main()
    else:
        #add interface to allow command line options ot be added
        main()