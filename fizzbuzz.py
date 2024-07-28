#Write a Python program that prints the numbers from 1 to 100. If the number is dividable by 3 print Fizz, 
# if the number is dividable by 5 print Buzz instead of the number. 
#If the number is dividable by 3 and 5 print FizzBuzz instead of the number.
# add your code here

fizzy = range(1,101)
def fizzbuzz():
    for x in fizzy:
        if x % 3 == 0 and x % 5 == 0:
            x = 'FizzBuzz'
            print(x)
        elif x % 5 == 0:
            x = 'Buzz'
            print(x)
        elif x % 3 == 0:
            x = 'Fizz'
            print(x)
        else:
            print(x)
    
fizzbuzz()

