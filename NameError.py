#this is a program to handle the name error 
#name error arises due to undeclared identifier or misspelled identifiers
# identifiers are python keywords, user defined variables or functions or classes etc

try:
    fullname = input("Enter your full name: ")
    #here an attempt is being made to print the variable name that doesnt exist hence error raises
    print(fullnam)
except NameError as err:
    print("error: ",err)