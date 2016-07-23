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
import copy

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
        tempList = []
        tempDictCoOrd = copy.deepcopy(cL.updatedCharDict[char]['Properties']['CoOrd'][:])

        for CoOrds in tempDictCoOrd:
            CoOrds[0] += spacing
            tempList.append(CoOrds)

        convertedMsg.append(tempList)

        spacing += cL.updatedCharDict[char]['Properties']['CharLength']
    return convertedMsg

def argParseFunc():
    import argparse
    import textwrap

    parser = argparse.ArgumentParser(prog='MessageDiplayUnicornHat',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=textwrap.dedent(
                                         '''
                                         *** Display user message on UnicornHat ***\n

                                         Input message as a string i.e. quotations; single (') or double (")

                                         E.g.  -m 'Hello' or --message "Hi"
                                     '''))

    parser.add_argument('-m', '--message', nargs=1, type=str,
                        help='Enter message you wish to display on UnicornHat', metavar='Message')

    args = parser.parse_args()

    return (args.message[0])

def main(msg):
    print(characterConverter(messageConvertToList(msg)))


if __name__ == '__main__':
    '''If program ran without without arguments (sys.argv == 1, ie main.py), run through userInput function'''
    if len(sys.argv) == 1:
        main(userInput())
    else:
        '''Else it will run argParseFunc function, using the arguments give when program was ran in command line. (>> python main.py -m "Hi")'''
        print(sys.argv)
        main(argParseFunc())
