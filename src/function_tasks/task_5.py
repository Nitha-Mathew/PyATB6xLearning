# Write a function, is_vowel that returns the value true if a given character is a vowel,
# and otherwise returns false.
# Write another function main, in main() function accept a string from user and count number
# of vowels in that string.

def is_vowel(x):
    if x in "aeiouAEIOU":
        return True
    else:
        return False


def main():
    str1 = input("Enter the string: ")
    c = 0
    for i in str1:
        y = is_vowel(i)
        if y:
            c = c + 1
    return c


main()
