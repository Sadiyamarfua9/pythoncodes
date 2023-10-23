x = input("Enter Month: ")

if x == 'January' or x == 'March' or x == 'May' or x == 'July' or x == 'August' or  x == 'October' or x == 'December':
    print("31")
elif x == "April" or x == "June" or x == "September" or x == "November":
    print("30")
elif x == "February":
    print("28")
else:
    print("Invalid")
