
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
add = num1 + num2
sub = num1 - num2
mul = num1 * num2
if num2 != 0:
    div = num1 / num2
else:
    print("Cannot divide with 0")

print("\nAddition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ",mul)
print("Division: ", div)