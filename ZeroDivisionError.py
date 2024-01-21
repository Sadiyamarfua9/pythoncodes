def div(a,b):
  try:
    res=a/b
  except ZeroDivisionError as ze:
    print("not allowed as {ze}")
  else:
    print("result is:",res)
  finally:
    print("division is successfully done")
a=int(input("enter number1:\n"))
b=int(input("enter number2:\n"))
div(a,b)
