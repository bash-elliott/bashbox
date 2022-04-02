from bashbox import bashbox

box = bashbox()
box.setColumns(3)
box.setTheme('curved')
box.setTitle("Friends")
box.setText(0, "Bob", "Regina", "Terry")
box.setText(1, "bobtheman@email.com", "regina.disney@email.com", "terrymaster@email.com")
box.setText(2, "+1 (111) 222-3333", "+1 (444) 555-666", "+1 (777) 888-9999")
box.draw()