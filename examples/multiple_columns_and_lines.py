from bashbox import bashbox

box = bashbox()

box.setColumns(2)
box.setText(0, "Here's a column with one line.")
box.setText(1, "Here's another column", "with two lines!")
box.draw()