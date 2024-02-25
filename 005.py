solution=0
n=1
z=0
def solve(x,y):
    global z
    if x%y==0 and y>1:
        solve(x,y-1)
    if y==1:
        z=True
    pass

while True: 
    solve(n,20)
    if z==True:
        break
    else:
        n+=1
solution=n
print(solution)
