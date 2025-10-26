n=int(input("Enter the limit: "))
num=n
fact=1
#while n>0:
#    fact=fact*n
#    n=n-1
#print(f"factorial of {num} is {fact}")

for i in range(n,0,-1):
    fact=fact*i
print(f"factorial of {num} is {fact}")


