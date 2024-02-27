n=1
solution=0
z=2
def isPrime(x):
    n=2
    while n<x:
        if x%n==0:
            return False
        n=n+1
    return True

while n<=10001:
    if isPrime(z):
        solution=z
        n=n+1
    z=z+1
        
print(solution)
