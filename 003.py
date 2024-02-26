solution=0
n=1
z=600851475143
def solve(x):
    n=2
    while n<x:
        if x%n==0:
            return False
        n=n+1
    return True

while n<=z:
    if solve(n) and z%n==0:
        z=z/n
        solution=n
    n=n+1

print(solution)
