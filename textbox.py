CornerTL = "\u2554"
CornerTR = "\u2557"
CornerBL = "\u255a"
CornerBR = "\u255d"
EdgeH = "\u2550"
EdgeV = "\u2551"
SplitU = "\u2566"
SplitR = "\u2563"
SplitL = "\u2560"
SplitD = "\u2569"

# Generates a dynamically sized box to hold text.
def simpleBox(text = []):

    # Initialize max variable
    max = 0

    # Length of longest string
    for i in range(len(text)):
        if len(str(text[i])) > max:
            max = len(str(text[i]))

    # Prints the top row of the box.
    print(CornerTL + (EdgeH * (max + 2)) + CornerTR )

    # Loops through every string in the text list and prints it inside the box.
    for i in range(len(text)):
        print(EdgeV + " " + str(text[i]) + (" " * (max - len(str(text[i])) + 1)) + EdgeV)

    # Prints the bottom row of the box.
    print(CornerBL + (EdgeH * (max + 2)) + CornerBR )

# Generates a dynamically sized box to hold two columns of text.
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

    # Prints the top row of the box.
    print(CornerTL + (EdgeH * (maxA + 2)) + SplitU + (EdgeH * (maxB + 2)) + CornerTR )

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

        print(EdgeV + " " + currentTextA + (" " * (maxA - len(currentTextA) + 1)) + EdgeV + " " + currentTextB + (" " * (maxB - len(currentTextB) + 1)) + EdgeV 
        )
    
    # Prints the bottom row of the box.
    print(CornerBL + (EdgeH * (maxA + 2)) + SplitD + (EdgeH * (maxB + 2)) + CornerBR )

def colBox(*inputs):
    texts = []
    maxes = []
    currentTexts = []
    inputs = list(inputs)
    for i in range(len(inputs)):
        texts.append(list(inputs[i]))
    
    for i in range(len(texts)):
        maxes.append(0)
        for j in range(len(texts[i])):
            if len(str(texts[i][j])) > maxes[i]:
                maxes[i] = len(str(texts[i][j]))

    rowMax = len(max(texts))

    t = CornerTL
    for i in range(len(maxes)):
        t += EdgeH * (maxes[i] + 2)
        if i < len(maxes) - 1:
            t += SplitU
    t += CornerTR

    mA = []
    for i in range(rowMax):
        m = ""
        for j in range(len(texts)):
            try:
                currentTexts.append(str(texts[j][i]))
            except:
                currentTexts.append("")
        m += EdgeV
        for j in range(len(currentTexts)):
            m += " " + currentTexts[j] + (" " * (maxes[j] - len(currentTexts[j]) + 1))
            m += EdgeV
        currentTexts = []
        mA.append(m)
    m += EdgeV

    b = CornerBL
    for i in range(len(maxes)):
        b += EdgeH * (maxes[i] + 2)
        if i < len(maxes) - 1:
            b += SplitD
    b += CornerBR

    print(t)
    for i in range(len(mA)):
        print(mA[i])
    print(b)

colBox(["Person A", "Person B", "", "Person D"], ["20", "", "21", "22"], ["Female", "", "Male", ""], ["", "", "", "Yes"])