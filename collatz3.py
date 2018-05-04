#Version 2 of Collatz number exercise

print('Enter a number: ')
number = int(input())

running = True

while running:
    if number % 2 == 0:
    
        number = number / 2
        print(number)
        

        if number == 1:  #only need one of these end break conditions. Not need to repeat in the else statment
            break
    
    else:
 
        number = (3*number +1)
        print(number)
        
        #deleted number = number from both if and else. Looks like no need to
        #rede fine number using yet another variable.


        




        
