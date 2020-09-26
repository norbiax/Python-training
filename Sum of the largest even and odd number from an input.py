import random
import numpy as np
A=[]
ans = "Y"
while ans == "Y":
    try:
        N = int(input("Please enter number of elements: "))
        for i in range(0, N):
            while True:
                try:
                    elem = int(input("Enter number " + str(i+1) + ": "))
                    A.append(elem)
                except:
                    print("Entered value is a string. Must be a number")
                    continue
                break
        ans = False

    except ValueError:
        print("Entered value is not an integer.")
        ans = input("Would like to try again? [Y/N]")

def solution(A):
    print(A)
    largest_odd = 0
    largest_even = 0

    for num in A:
        if num % 2 != 0 and num > largest_odd:
            largest_odd = num
    if largest_odd == 0:
        print("There were no odd integers")
    else:
        print("The largest odd number is:", largest_odd)

    for num in A:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    if largest_even == 0:
        print("There were no even integers")
    else:
        print("The largest even number is:", largest_even)

    print("Sum:", largest_odd + largest_even)


solution(A)