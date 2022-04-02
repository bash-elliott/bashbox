from bashbox import bashbox

box = bashbox()
box.setColumns(2)
box.setText(0, "Some Text!")
box.setText(1, "Another column of text!")
box.draw()