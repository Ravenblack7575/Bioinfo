# This program is for calculating copy number of genetic material with selection by user.

# This program incorporates library function.
# This program loops back to the beginning.



def askUser():
    while True:
        try:
            choice = int(input("Do you want to: \n(1) Calculate DNA copies \n(2) Calculate ssDNA copies \n(3) Calculate RNA copies \n(4) Convert moles to grams \n(5) Convert grams to moles \n"))
        except ValueError:
            print("Please input a number")
            continue
        if 0 < choice < 6:
            break
        else:
            print("That is not between 1 and 5! Try again:")
    print ("You entered: {} ".format(choice))

    def copynumDNA():
        print('')
        print('Enter amount of DNA to be calculated (ng): ')
        amtDNA = input(float)

        print('')
        print('Enter length of DNA (bp): ')
        lengthDNA = input(float)

        resultCopy =(float(amtDNA) *(6.0221*10**23)) / (int(lengthDNA) * (660*1*10**9))

        print('')
        print('The answer is', resultCopy, 'copies.')
        print('')


    def copynumssDNA():
        print('')
        print('Enter amount of DNA to be calculated (ng): ')
        amtssDNA = input(float)

        print('')
        print('Enter length of DNA (bp): ')
        lengthssDNA = input(float)

        resultCopy =(float(amtssDNA) *(6.0221*10**23)) / (int(lengthssDNA) * (330*1*10**9))

        print('')
        print('The answer is', resultCopy, 'copies.')
        print('')


    def copynumRNA():
        print('')
        print('Enter amount of RNA to be calculated (ng): ')
        amtRNA = input(float)

        print('')
        print('Enter length of RNA (bp): ')
        lengthRNA = input(float)

        resultCopy =(float(amtRNA) *(6.0221*10**23)) / (int(lengthRNA) * (340*1*10**9))

        print('')
        print('The answer is', resultCopy, 'copies.')
        print('')

    def molestoGram():
        print('')
        print('Enter the amount of genetic material to convert (moles):')
        amtMole = input(float)

        print('')
        print('Enter the molecular weight of the molecule (g/moles):')
        molWeight = input(float)

        resultGram =(float(amtMole) * float(molWeight))

        print('')
        print('The answer is ', resultGram, ' g.')
        print('')


    def gramstoMoles():
        print('')
        print('Enter the amount of genetic material to convert (grams):')
        amtGrams = input(float)

        print('')
        print('Enter the molecular weight of the molecule (g/moles):')
        molWeight = input(float)

        resultMoles =(float(amtGrams) / float(molWeight))

        print('')
        print('The answer is ', resultMoles, ' moles.')
        print('')

    mydict = {1:copynumDNA, 2:copynumssDNA, 3:copynumRNA, 4:molestoGram, 5:gramstoMoles}
    mydict[choice]()


askUser()

while True:  #For looping back to beginning.
    
    restart = input('Would you like to restart this program? (y/n) ')

    if restart == 'yes' or restart == 'y':
        askUser()
    if restart == "n" or restart == "no":
        print('Script terminating. Goodbye.')
        print('')
        break

