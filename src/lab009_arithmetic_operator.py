a=float(input("Enter first number:"))
b=float(input("Enter second number:"))

sum=a+b #addition
sub=a-b #subtraction
mul=a*b #multiplication
div=a//b #floor division
div2=a/b #nteger division
div3=a%b #remainder
div4=divmod(a,b)
print(sum,sub,mul,div,div2,div3,div4, sep="   |   ")