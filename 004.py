def is_palindromic(x):
    length=len(str(x))
    if int(str(x)[:length+1])==int(str(x)[length+1::-1]):
        return True
    return False
x=100
y=100
solution=0
while y<999:
    if is_palindromic(x*y) and x*y>=solution:
        solution=(x*y)
        print(x,y)
    x=x+1
    if x==999:
        y=y+1
        x=100

print(x,y)
print(solution)
