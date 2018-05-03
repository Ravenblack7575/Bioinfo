#This exercise teaches about parameters and arguments

def do_twice(f,v): #function as argument, value as argument)
	f(v)
	f(v)

def print_spam(v): #print a variable
	print(v)
	

do_twice(print_spam, 'bingo') #(f = print spam function, v = string value 'bingo') 


def do_four(f,v):
	do_twice(f,v)
	do_twice(f,v)
	
	
do_four(print_spam, 'shit')