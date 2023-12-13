n=int(input("enter the limit: "))
x=0
y=1
count=0
while count<n:
    if n<0:
        print("positive numbers are only allowed")
    else:
        print(x,end=" ")
        z=x+y
        x=y
        y=z
        count+=1