# variable aguements are used to take multiple input variables/parameters into a function
# a function that displays names is defined. it uses var args to take and display many names 
def printnames(*args):
    # a for loop iterates through each name in the parameter
    for name in args:
        print(name)
        
# we call the function with many names
printnames('abc','def','ghi','jkl','mno')
 
# This program demonstrates the use of **kwargs in Python functions.
# The **kwargs syntax allows a function to accept a variable number of keyword arguments,
# providing flexibility when calling the function with different sets of named parameters.

def display_info(**kwargs):
    # Iterate over key-value pairs in the kwargs dictionary
    for key, value in kwargs.items():
        # Print each key-value pair
        print(f"{key}: {value}")

# Example usage
# Call the display_info function with multiple keyword arguments
display_info(name="John", age=25, city="New York", occupation="Engineer")
