#entrance to a club only if age in 21

Age=int(input("Enter your age: ").strip())
if (Age<0 or Age >130):
    print("Enter a valid age")
else:
    if Age<=21:
        print("not Eligible")
    else:
        print("eligible")
