## Simple calculator 

## Choose what operation you want to do
print("Simple Calculator, created by Timnik")
print("Select what operation you want to do: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print(" ")
x = int(input("Enter: "))
print(" ")

## Enter the 2 numbers
print("Select the two numbers:")
print(" ")
z = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
if (x==1):
    print(str(z) + " + " + str(y) + " = " + str(z + y))
elif (x==2):
    print(str(z) + " - " + str(y) + " = " + str(z - y))
elif (x==3):
    print(str(z) + " * " + str(y) + " = " + str(z * y))
elif (x==4):
    print(str(z) + " : " + str(y) + " = " + str(z / y))
else:
    print("You enter an invalid argument. The only valid arguments are: 1, 2, 3 or 4")
