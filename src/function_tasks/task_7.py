# Write the definition of a function zero_ending(scores) to add all those values in the list of scores,
# which are ending with zero and display the sum.
# For example: If the scores contain [200, 456, 300, 100, 234, 678] The sum should be displayed as 600
def zero_ending(scores):
    sum = 0
    for i in scores:
        if i % 10 == 0:
            sum = sum + i
    return sum


lst = [200, 456, 300, 100, 234, 678]
x = zero_ending(lst)
print(x)
