# Write a function named is_prime, which takes an integer as an argument and returns true
# if the argument is a prime number, or false otherwise.
# Also, write the main function that displays prime numbers between 1 to 500.

def isprime(a):
    if a<=1:
        return False
    else:
        for i in range(2,a-1):
            if a%i==0:
                return False
            else:
                return True
def main():
    lst=[]
    for j in range(1,501):
        y=isprime(j)
        if y:
            print(j,end=' ')
main()