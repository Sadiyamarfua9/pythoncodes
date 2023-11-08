n = int(input("Enter the number: "))
f = 1
if n == 1 or n == 0:
    print(f'Factorial of {n} is 1')
elif n<0:
    print(f' factorial of negative numbers not possible')
else:
    for i in range(2,n+1):
        f = f*i
    print(f'Factorial of {n} is {f}')
