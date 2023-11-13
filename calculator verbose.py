a=float(input("Enter the first value"))
b=float(input("Enter the second value"))
print("Type 1,2,3,4 for the following operations:")
print("Operation menu:\n1. Addition\n2. Substraction\n3. Multiplication\n4. Division")
op=input("Select Operation:")
if op=="1":
    print(a+b)
if op=="2":
    print(a-b)
if op=="3":
    print(a*b)
if op=="4":
    print(a/b)
else:
    print("Operation doesn't exist BITCH!")
print("Arigato🎎!")