# Write a definition of a method count_now(places) to find and display those place names,
# in which there are more than 5 characters.


def count_now(places):
    lst = []
    for i in places:
        if len(i) > 5:
            print(i)


lst = ["DELHI", "LONDON", "PARIS", "NEW YORK", "DUBAI"]
count_now(lst)

