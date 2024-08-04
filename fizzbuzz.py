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
