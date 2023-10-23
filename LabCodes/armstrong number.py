n = int(input("Enter number: "))
a=n
arm = 0
while n>0:
    rem = n%10
    arm = arm+ (rem*rem*rem)
    n//=10
    
if arm == a :
    print(a,' is armstrong')
else:
    print("not armstrong",arm)
