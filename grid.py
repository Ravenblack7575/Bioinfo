def do_four(f): #function as argument, value as argument)
	f()
	f()
	f()
	f()


def horizontal_bar():
	print('+ - - - - + - - - - +')
	
def column_bar():
	print('|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|')
	
horizontal_bar()
do_four(column_bar)
horizontal_bar()
do_four(column_bar)
horizontal_bar()