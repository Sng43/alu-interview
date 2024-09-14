#!/usr/bin/python3

"""
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

"""
def minOperations(n):
    if n <= 1:
        return 0
    
    divisor = 2

    number_of_operations = 0

    while n > 1:
        if n % divisor == 0:
            n = n / divisor

            number_of_operations = number_of_operations + divisor

        else:
            divisor +=1

    return number_of_operations

n = 9

print(minOperations(n))
