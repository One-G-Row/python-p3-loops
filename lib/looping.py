#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    count = 1

    while i > 0:
        print(i)
        i -= count
    
    print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    double_list = []
    for int in int_list:
        double = int ** 2
        double_list.append(double)
    return double_list

square_int = square_integers([1, 2, 3, 4, 5])
print(square_int)

def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        
fizzbuzz()
        