f=open('File_Programs/sample1.txt')
#file opens in read mode by default
print(f.read())
#reads and prints all the contents of the file
f.seek(0)
#seek(0) resets the position of file pointer to the first letter of the document
print("\n",f.readline())
#prints only the first line
f.seek(0)
print(f.readlines())
#prints all the lines of the file into a list
f.close()
#closes the file after use