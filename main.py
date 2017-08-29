'''
Importing Librarys required for use of unicornhat
    -unicornhat
    -time, to allow wait states
    -character_library has characters created in a 8x8 matrix, will check message to make sure all characters available
'''

import unicornhat as UH
import time
import character_library as cL
import sys
import copy

def userInput():
    '''
    Simple userInput function to keep the design simple on the console
    '''

    
    Message = (input("\nInput: "))
    return  Message


def messageConvertToList(msg):
    '''
    Converts a string to a list of characters
    msg: string Message
    return: list with all characters including whitespace
    '''

    
    listMsg = []
    for char in msg.upper():
        listMsg.append(char)
    return listMsg

def characterConverter(listMsg):
    '''
    Converts the list message to a list of co-ordinates [x,y] with the appropriate spacing between letters.
    The function uses the import of characerLibrary which is a seperate python file which contains only a dictionary of characters.
    A seperate file allows users to change FONT styles by simply repleacing the exsisting file to anything else.
    listMsg: Message to be converted
    return: converted Message in [X,Y] with appropriate spacing
    '''


    convertedMsg = []
    
    #spacing takes the first char length
    #i.e. starts with a blank screen for the first frame and second frame is the start of the message.    
    spacing = cL.updatedCharDict[listMsg[0]]['Properties']['CharLength']
    #loops through each character in list
    for char in listMsg:

        #list used to store each characters Co-Ordinates which they are beign converted
        tempList = []
        
        #references character_library dictionary for the Co-Ordinates and creates a temp variable
        tempDictCoOrd = copy.deepcopy(cL.updatedCharDict[char]['Properties']['CoOrd'][:])

        #loops through each Co-Ordinate in the temp variable once finished it adds tempList to the end of convertedMsg list
        for CoOrds in tempDictCoOrd:

            #subtracts the previous characters spacing so there is no overlaping of characters
            CoOrds[0] -= spacing
            
            tempList.append(CoOrds)

        #adding completed character conversion with spacing to end of the convertedMsg list
        convertedMsg.extend(tempList)

        #saves the currents characters spacing to be used on the next characters conversion to stop overlapping 
        spacing += cL.updatedCharDict[char]['Properties']['CharLength']
    return convertedMsg


def argParseFunc():
    '''
    argParseFunc allows users to quickly get a scrolling message started using the command line only.
    Only imports argparse and textwrap when required.
    '''

    
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


def animation(listConv):
    '''
    The functions takes the converted list and loops through it by add 1 to the X values of each Co-Ordinate i.e. (0,0),(1,1) becomes (1,0),(2,1).
    If the Co-Ordinates X-axis do not site between 7 and 0 they are ignored and only Co-Ordinates between these values will be shown.
    It runs through the listConv only once
    listConv: list of the converted message to [x,y] with appriate spacing
    '''


    #determines the smallest X value from the converted list and subtracts 9 to allow for the entire message to be shown
    #and not cut off when the last character is shown i.e. last character moves the entire length of the "screen"
    animationLength = min(min(listConv)) - 9

    #looping through the listConv once
    while animationLength < 0:

        #looping through each Co-Ordinate getting the index and variable
        for index, var in enumerate(listConv):

            #if X variable is between 7 & 0 it will set up the pixel on the unicorn hat in white
            if ((var[0] > -1) & (var[0] < 8)):
                UH.set_pixel(var[0],var[1],255,255,255)
            #adds 1 to X value of each Co-Ordinate to push the message from right to left
            listConv[index][0] += 1

        #once looped through entire Co-Ordinate list it will show the set pixel
        UH.show()
        time.sleep(0.1)
        #clears all the set pixels but will not switch off pixels as once they are set they stay on until pixels unset or .clear() and a .show() is ran again
        UH.clear()
        #animationLength is incremented while loop will stop once entire message is shown
        animationLength += 1




def main(msg):
    '''
    main function uses all the functions above to create a variable called Frames which has the converted message in [X,Y] Co-Ordinates.
    Loops the message continously.
    '''

    #Frames contains the converted message in [X,Y] Co-Ordinates
    Frames = ((characterConverter(messageConvertToList(msg))))
    
    #loops continously untill program stopped
    while True:
        
        #As Co-Ordinates get manipulted another variable is created and a deep copy of the Frame is used (Pass by Value rather than reference).
        loopFrames = copy.deepcopy(Frames)
        animation(loopFrames)


#Program is only to be used if this is the main program and not imported in to another program.
if __name__ == '__main__':
    '''If program ran without without arguments (sys.argv == 1, ie print (sys.argv) == [main.py]), run through userInput function'''
    if len(sys.argv) == 1:
        main(userInput())
    else:
        '''Else it will run argParseFunc function, using the arguments give when program was ran in command line. (>> python main.py -m "Hi")'''
        main(argParseFunc())
