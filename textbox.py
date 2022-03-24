# Generates a dynamically sized box to hold text.
def simpleBox(text = []):

    # Initialize max variable
    max = 0

    # Length of longest string
    for i in range(len(text)):
        if len(str(text[i])) > max:
            max = len(str(text[i]))

    # Sets the characters for the box's corners (cornerChars) and walls (edgeCharV and edgeCharH, corresponding to vertical wall and horizontal wall respectively).
    # cornerChars works as an array: top left [0], top right [1], bottom left [2], bottom right [3]
    # Can take in any unicode character, but works best with the unicode character codes.
    # \u2554 = ╔
    cornerChars = ["\u2554", "\u2557", "\u255a", "\u255d"]
    edgeCharV = "\u2551"
    edgeCharH = "\u2550"

    # Prints the top row of the box.
    print(cornerChars[0] + (edgeCharH * (max + 2)) + cornerChars[1] )

    # Loops through every string in the text list and prints it inside the box.
    for i in range(len(text)):
        print(edgeCharV + " " + str(text[i]) + (" " * (max - len(str(text[i])) + 1)) + edgeCharV)

    # Prints the bottom row of the box.
    print(cornerChars[2] + (edgeCharH * (max + 2)) + cornerChars[3] )

def twoColBox(textA = [], textB = []):
    textA = list(textA)
    textB = list(textB)

    maxA = 0
    maxB = 0

    for i in range(len(textA)):
        if len(str(textA[i])) > maxA:
            maxA = len(str(textA[i]))
    
    for i in range(len(textB)):
        if len(str(textB[i])) > maxB:
            maxB = len(str(textB[i]))

    rowMax = max([len(textA), len(textB)])

    # Sets the characters for the box's corners (cornerChars) and walls (edgeCharV and edgeCharH, corresponding to vertical wall and horizontal wall respectively).
    # cornerChars works as an array: top left [0], top right [1], bottom left [2], bottom right [3]
    # splitChars works as an array: top split [0], bottom split [1],
    # Can take in any unicode character, but works best with the unicode character codes.
    # \u2554 = ╔
    cornerChars = ["\u2554", "\u2557", "\u255a", "\u255d"]
    splitChars = ["\u2566", "\u2569"]
    edgeCharV = "\u2551"
    edgeCharH = "\u2550"

    # Prints the top row of the box.
    print(cornerChars[0] + (edgeCharH * (maxA + 2)) + splitChars[0] + (edgeCharH * (maxB + 2)) + cornerChars[1] )

    # Loops through every string in the text list and prints it inside the box.
    for i in range(rowMax):
        try:
            currentTextA = str(textA[i])
        except:
            currentTextA = ""

        try:    
            currentTextB = str(textB[i])
        except:
            currentTextB = ""

        print(
            edgeCharV + 
            " " + 
            currentTextA + 
            (
                " " * (maxA - len(currentTextA) + 1)
            ) + 
            edgeCharV + 
            " " + 
            currentTextB + 
            (
                " " * (maxB - len(currentTextB) + 1)
            ) + 
            edgeCharV 
        )
    
    # Prints the bottom row of the box.
    print(cornerChars[2] + (edgeCharH * (maxA + 2)) + splitChars[1] + (edgeCharH * (maxB + 2)) + cornerChars[3] )

twoColBox(
    [
        "Name", 
        "Age", 
        "Sex"
    ], 
    [
        "Bash Edward Elliott", 
        "17", 
        "Male"])