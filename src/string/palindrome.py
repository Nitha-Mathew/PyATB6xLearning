word=input("Enter the word: ")
word.strip()
reversed_word=word[::-1]
if word==reversed_word:
    print("It is a palindrome")
else:
    print("It is a not palindrome")