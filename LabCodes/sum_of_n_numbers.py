n=int(input("Enter a number: "))
add = 0
for i in range(1,n+1):
    print(i,end = " ")
    if i<n:
        print('+', end = '')
    add+=i
print(f'sum of {n} numbers is : {add}')
