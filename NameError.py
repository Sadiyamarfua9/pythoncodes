#this is a program to handle the name error 
#name error arises due to undeclared identifier or misspelled identifiers
# identifiers are python keywords, user defined variables or functions or classes etc

try:
    fullname = input("Enter your full name: ")
    #here an attempt is being made to print the variable name that doesnt exist hence error raises
    print(fullnam)
except NameError as err:
    print("error: ",err)

#program2 for NameError
try:
  n1=int(input("enter number1:\n"))
  n2=int(input("enter number2:\n"))
  #here an attempt is being made to print the result after adding two numbers
  print(res)
 #since print statement is written before logic therefore an error raises
res=n1+n2
except NameError as ne:
  print(f"{ne}")
