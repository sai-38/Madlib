"""
    This program takes a mad lib text file
    and will output a new string containing the solved
    mad lib.
    The mad lib is solved one user entered word at a time.
"""

#opening the MadLib text file
madlib = open("MadLib.txt", "r")

#assigning the contents of the file as a string
mad = madlib.read()



#creating the function to solve a mad lib
def madLib(mad):
    #new will contain all the chunks of the mad lib as it
    #is solved. last keeps track of the index of the last
    #solved placeholder.
    new = ""
    last = 0
    for index in range(len(mad)):
        #"[" and "]" identify the start and end of a placeholder.
        #this if elif keeps track of the placeholder's index.
        if mad[index] == "[":
            start = index
        elif mad[index] == "]":
            end = index
            #askFor hold the word type: Noun, Verb... to ask
            #the user to input.
            askFor = mad[start+1:end]

            #the try block asks for a user input and formats
            try :
                replace = input("Please enter a {}: ".format(askFor))
                #new holds the mad lib solved so far.
                new = new + mad[last:start] + replace
                #last keep traks of the index the mad lib has been
                #solved to  so far
                last = end+1
            except:
                print("Unexpected error occured")
                break
    #This ensures the end of the mad lib is added to new.
    new += mad[end+1:]
    return new


with open("MadLibAnswer.txt", "a") as answer:
    answer.write(madLib(mad)+"\n")
