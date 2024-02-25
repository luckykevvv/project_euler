n=0
solution=0
while n<1000:
    if n%3==0 or n%5==0:
        solution+=n
    n=n+1
print(solution)
