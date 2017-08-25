#   main.py
#   LastDigit_Python
#
#   This program will give you the name of the las digit of the addition of any two given numbers
#
#   Python interpreter: 3.6
#
#   Author: León Felipe Guevara Chávez
#   email:  leon.guevara@itesm.mx
#   date:   May 31, 2017
#

#   We ask for and read two whole numbers
number1 = int(input("Give me the first number: "))
number2 = int(input("Give me the second number: "))

#   We compute the addition of both numbers and the last digit of such addition
addition = number1 + number2
remainder = addition % 10

#   We display the name of the last digit
if remainder == 1:
    print("one")
elif remainder == 2:
    print("two")
elif remainder == 3:
    print("trhee")
elif remainder == 4:
    print("four")
elif remainder == 5:
    print("five")
elif remainder == 6:
    print("six")
elif remainder == 7:
    print("seven")
elif remainder == 8:
    print("eight")
elif remainder == 9:
    print("nine")
else:
    print("zero")
