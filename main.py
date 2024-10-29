def power(n):
    if n<=0:
        return False
    return (n&(n-1))==0
n=int(input("Enter a number: "))
if power(n):
    print("It is a power of 2")
else:
    print("It is not a power of 2")
