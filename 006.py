solution=0
n=1
sum=0
sqare=0
while n<=100:
    sum+=n**2
    sqare+=n
    n+=1
sqare=sqare**2
solution=sqare-sum    
print(solution)
