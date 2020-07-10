from tkinter import *

window = Tk()# an instance of the Tkinter class
window.title("Calculator")

entry = Entry(window,border = 10, width = 35)
entry.grid(row = 0,column = 0,padx = 10, pady = 10,columnspan = 3)

def button_click(number):
	current = entry.get()
	entry.delete(0,END)
	entry.insert(0,int(str(current) + str(number)))


def button_add():
	first_num = entry.get()
	global f_num
	f_num = int(first_num)
	entry.delete(0,END)
	return

def button_equal():
	second_num = entry.get()
	entry.delete(0,END)
	entry.insert(0,f_num + int(second_num))

def button_clear():
	entry.delete(0,END)


def create_number_buttons():
	number_buttons,text= [],"0"
	number = 0
	for i in range(10):
		text = str(int(text) + 1)
		number += 1
		# print(num)	
		if i == 9:
			text = "0"
			number = 0
		button = "Button(window,text = text,padx = 40,pady = 20,command = lambda:button_click{})".format(number) 
		# print(number)
		number_buttons.append(button)

	return number_buttons
print()

def create_add_button():
	add_button = Button(window,text = "+",padx = 39,pady = 20,command = button_add)
	return add_button

def create_equal_button():
	equal_button = Button(window,text = "=",padx = 91,pady = 20,command = button_equal)
	return equal_button

def create_clear_button():
	clear_button = Button(window,text = "clear",padx = 79,pady = 20,command = button_clear)
	return clear_button

number_buttons = create_number_buttons()
print(number_buttons)
add_button = create_add_button()
equal_button = create_equal_button()
clear_button = create_clear_button()

def apply_grid():
	# row,column = 3,0
	for i in range(len(number_buttons)):
		if i % 3 == 0:
			column = 0
		elif i % 3 == 1:
			column = 1
		else:
			column = 2
		if i < 3:
			row = 3
		elif i < 6:
			row = 2
		elif i == 9:
			row = 4
			column = 0
		else:
			row = 1
		# print(number_buttons[i])

		number_buttons[i].grid(row = row,column = column)

	add_button.grid(row = 5,column = 0)
	equal_button.grid(row = 5,column = 1, columnspan = 2)
	clear_button.grid(row = 4, column = 1, columnspan = 2)


apply_grid()


window.mainloop()

