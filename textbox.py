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

class TextBox:
    """
    Standard textbox.
    """
    def __init__(self):
        self.columns = 1
        self.text = [[]] * 1

    def setColumns(self, num):
        """
        Sets the number of columns for the textbox.

        num: the number of columns. Defaults to 1.
        """
        self.columns = num
        self.text = [[]] * num

    def setText(self, col, *text):
        """
        Sets the text for a given column.

        col: the column to set the text for.
        text: the text to set. Can take multiple strings.

        NOTE: use setColumns first to set the number of columns before setting text.
        """
        self.text[col] = list(text)
    
    def draw(self):
        """
        Draws the textbox.
        """
        texts = list(self.text)
        maxes = []
        currentTexts = []
        # for i in range(len(inputs)):
        #     texts.append(list(inputs[i]))
        
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