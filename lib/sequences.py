#!/usr/bin/env python3

def print_fibonacci(length):
    #if length is zero, return empty list "[]\n"
    if length == 0:
        return "[]\n"
    elif length == 1:
        return "[0]\n"
    # if length is 1, print 0
    # if length is greater than 1, generate fibonacci sequence up to provided length. while loop to add new elements until it reaches the provided length
    else:
        fibonacci_list = [0, 1]
        while len(fibonacci_list) < length:
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            # append the next number to fibonacci_list 
            fibonacci_list.append(next_number)
        return fibonacci_list


