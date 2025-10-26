# Write a Python program to count the number of strings having length more than 2 and are palindrome in a list using loop.
# Input:- ['ab', 'abc', 'aba', 'xyz', '1991']
# Output:- 2

lst = ['ab', 'abc', 'aba', 'xyz', '1991']
p = 0
for i in lst:
    c = 0
    if len(i) > 2:
        k = -1
        for j in range(0, len(i), 1):
            if i[j] != i[k]:
                break
            else:
                k = k - 1
                c = c + 1
    if c == len(i):
        p = p + 1
print(p)

