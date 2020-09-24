import random
import numpy as np

def solution():
    rand_nums = np.random.randint(1, 1000, 10)
    print(rand_nums)
    largest_odd = 0
    largest_even = 0

    for num in rand_nums:
        if num % 2 != 0 and num > largest_odd:
            largest_odd = num
    if largest_odd == 0:
        print("There were no odd integers")
    else:
        print("The largest odd number is:", largest_odd)

    for num in rand_nums:
        if num % 2 == 0 and num > largest_even:
            largest_even = num
    if largest_even == 0:
        print("There were no even integers")
    else:
        print("The largest even number is:",largest_even)

    print("Sum:", largest_odd+largest_even)

solution()