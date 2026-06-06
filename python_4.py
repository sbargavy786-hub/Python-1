a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
print(f"a = {a}, b = {b}")
one = a + b # This is a comment explaining that this line calculates the sum of a and b
two = a - b # This line calculates the difference between a and b
three = a * b # This line calculates the product of a and b
four = a / b # This line calculates the quotient of a and b
five = a ** b # This line calculates a raised to the power of b
six = a // b # This line calculates the floor division of a by b
seven = a % b # This line calculates the remainder of a divided by b
eight = (a + b) * (a - b) # This line calculates the product of the sum and difference of a and b
nine = (a * b) / (a + b) # This line calculates the quotient of the product and sum of a and b
print(f"a+b = {one}") 
print(f"a-b = {two}")
print(f"a*b = {three}")
print(f"a/b = {four}") 
print(f"a**b = {five}")
print(f"a//b = {six}")
print(f"a%b = {seven}")
print(f"(a+b)*(a-b) = {eight}")
print(f"(a*b)/(a+b) = {nine}")
print(f"Round the last answer to 2 decimal places: {round(nine, 2)}")
print(f"a+b = {a+b}")
print(f"a-b = {a-b}")
print(f"a*b = {a*b}")

