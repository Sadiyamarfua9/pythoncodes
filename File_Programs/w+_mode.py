path='File_Programs/sample2.txt'
f=open(path,'w+')
line=input("Enter a line of string: ")
f.write(line)
#write function writes the string taken from user into the file
f.seek(0)
#pointer reset to first element of file
Lines=[]
while True:
    line=input("Enter line (type EOF to end): ")
    if line == 'EOF':
        break
    Lines.append(line)
#while loop executes and stores each element in a list until the user enters EOF
inputstring = "\n".join(Lines)
#join function joins the elements of the list into a string and between each element it places \n to print a new line
f.writelines(inputstring)
#writelines allows us to write multiple lines of code 
f.seek(0)
print("----\nContents of the file:")
print(f.read())
f.close()
