# Write a function getSumOfLastDigits() that takes in a list of positive numbers and returns the sum of all the last digits in the list.


def getSumOfLastDigits(lst):
    s = 0
    for i in lst:
        a = i % 10
        s = s + a
    return s


getSumOfLastDigits([1, 23, 456])

