#adding up some title
print('CHECK WHICH IS PALINDROME AND NOT IN THE GIVEN NUMBER')

#it display the number you just type
digital = int(input('\nTYPE 3 NUMBERS TO DEFINE IF ITS PALINDROME OR NOT :   '))
print('GIVEN =', digital)

#it defines the given 
define_integers = str(digital)

#it display the reversed number
check_num = define_integers[::-1]
print('\nIN REVERSED: ', check_num)

#function to define if the given is palidrome number
if define_integers == check_num:
    print('\nThe given numerical is', check_num, 'and it is defines as apalidrome number\n')

#function to define if the given is not palidrome number 
else :
    print('\nThe given numerical is', check_num, 'and it is defines as not palidrome number.\n')