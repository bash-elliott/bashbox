import os

# from .bashbox import bashbox as bashbox

root = os.path.dirname(os.path.abspath(__file__)) + "\\.."

if not os.path.exists(root + "\\bashbox_init.txt"):
    os.mkdir(root + "\\bashbox_themes")
    with open(root + "\\bashbox_themes\\barebone.bsh", "w") as f:
        f.write("\\u002b\n\\u002b\n\\u002b\n\\u002b\n\\u002d\n\\u007c\n\\u002b\n\\u002b\n\\u002b\n\\u002b")
    with open(root + "\\bashbox_themes\\curved.bsh", "w") as f:
        f.write("\\u256D\n\\u256E\n\\u2570\n\\u256f\n\\u2500\n\\u2502\n\\u252c\n\\u2524\n\\u251c\n\\u2534")
    with open(root + "\\bashbox_themes\\double.bsh", "w") as f:
        f.write("\\u2554\n\\u2557\n\\u255a\n\\u255d\n\\u2550\n\\u2551\n\\u2566\n\\u2563\n\\u2560\n\\u2569")
    with open(root + "\\bashbox_themes\\example._bsh", "w") as f:
        f.write("Top Left Corner\nTop Right Corner\nBottom Left Corner\nBottom Right Corner\nHorizontal Line\nVertical Line\nHorizontal Split Going Down\nVertical Split Going Right\nVertical Split Going Left\nHorizontal Split Going Up\n")
    with open(root + "\\bashbox_themes\\single.bsh", "w") as f:
        f.write("\\u250c\n\\u2510\n\\u2514\n\\u2518\n\\u2500\n\\u2502\n\\u252c\n\\u2524\n\\u251c\n\\u2534")
    
    with open(root + "\\bashbox_init.txt", "w") as f:
        f.write("you smell pretty. :)")