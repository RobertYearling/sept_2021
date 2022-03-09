# Given an array with multiple values, write a function that returns a new array that
# only contains the maximum, minimum, and average values of the original array.
# (e.g. [1,5,10,-2] will return [10,-2,3.5])

# Function - Done
# Array - Done
# Variables

def min_max_avg(arr):
    min = 0
    max = 0
    avg = 0
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
        if arr[i] > max:
            max = arr[i]
        avg += arr[i]
    avg = avg / len(arr)
    new_arr = [min, max, avg]
    return new_arr

print(min_max_avg([1,5,10,-2]))


# What is the second largest value in the array [1,3,5,6,9]?
def second_largest(arr):
    largest = arr[0]
    second_largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    for num in arr:
        if num > second_largest and num != largest:
            second_largest = num
    return second_largest

print(second_largest([1,3,5,6,9]))


# Skyline Heights
# Lovely Burbank has a breathtaking view of the Los Angeles skyline. Let’s say you are
# given an array with heights of consecutive buildings, starting closest to you and extending
# away. Array [-1,7,3] would represent three buildings: first is actually out of view below
# street level, behind it is second at 7 stories high, third is 3 stories high (hidden behind
# the 7-story). You are situated at street level. Return array containing heights of buildings
# you can see, in order. Given [-1,1,1,7,3] return [1,7]. Given [0,4] return [4]. As always
# with challenges, do not use built-in array functions such as unshift().

def skyline(arr):
    new_arr = []
    biggest = 0
    for building in arr:
        if building > 0 and building > biggest:
            new_arr.append(building)
            biggest = building
    return new_arr

print(skyline([-1,1,1,7,3]))