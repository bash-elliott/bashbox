# Generates a dynamically sized box to hold text. Can take an unlimited number of string arguments. 
def startBox(*text):
    # The function takes in arguments using the * operator, which enters all of the arguments into a tuple. This function doesn't work with correctly with tuples, so this line of code converts it into a list.
    text = list(text)

    # Initialize the max variable, which is later used to determine the wideness of the resulting box.
    max = 0

    # Loops through every item in the list of strings, and sets max to the highest number AKA the length of the longest string.
    # Note: Use this code to make the max function later on.
    for i in range(len(text)):
        if len(text[i]) > max:
            max = len(text[i])

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
        print(edgeCharV + " " + text[i] + (" " * (max - len(text[i]) + 1)) + edgeCharV)

    # Prints the bottom row of the box.
    print(cornerChars[2] + (edgeCharH * (max + 2)) + cornerChars[3] )