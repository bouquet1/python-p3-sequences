#!/usr/bin/env python3

def print_fibonacci(length):
    #if length is zero, return empty list "[]\n". If length is 1, print '[0]\n'. "\n" adds a newline character at the end to format the output nicely.
    if length == 0:
        # return '[]\n'
        # return 0
        print("[]")
    elif length == 1:
        # return '[0]\n'
        # return 0
        print("[0]")
    # if length is greater than 1, generate fibonacci sequence up to provided length. while loop to add new elements.
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < length:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            # append the next number to fibonacci_list 
            fibonacci_list.append(next_number)
        # return "[" + ", ".join(map(str, fibonacci_list)) + "]\n"
        # return fibonacci_list 
        print(fibonacci_list)
    
        
        
# print(print_fibonacci(0)) => returns [] in terminal but the numbers are not separated by comma.
