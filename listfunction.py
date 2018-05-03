#Practice Project 4.1. Make a function that will print a list with commas and 'and'

list = []
while True:
	print('Enter name of thing that you want to put on the list ' + str(len(list)+1) + '(or enter nothing to stop.): ')
	
	name = input()
	if name == '':
		break
		
	list = list + [name]
	
print('Here\'s the list of things you\'ve condemned: " ')
#for i in range(len(list)-1):
print(list[0] + ', ' + list[+1] + 'and' + list[-1])
	#print((list[i] + ', ')) 
	#print('and ' + list[-1])