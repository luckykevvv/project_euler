solution=2
last=1
now=2
next=0
while next<4000000:
    next=last+now
    if next%2==0:
        solution+=next
    last=now
    now=next
print(solution)
