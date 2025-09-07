# Python Operators Example

a = 10
b = 3

print("Arithmetic Operators:")
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a ** b =", a ** b) # Exponentiation
print("a // b =", a // b) # Floor Division

print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("\nLogical Operators:")
x = True
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)

print("\nAssignment Operators:")
c = 5
c += 2
print("c after c += 2:", c)
c *= 3
print("c after c *= 3:", c)

print("\nBitwise Operators:")
print("a & b =", a & b)   # AND
print("a | b =", a | b)   # OR
print("a ^ b =", a ^ b)   # XOR
print("~a =", ~a)         # NOT
print("a << 1 =", a << 1) # Left shift
print("a >> 1 =", a >> 1) # Right shift

print("\nMembership Operators:")
list1 = [1, 2, 3, 10]
print("10 in list1:", 10 in list1)
print("5 not in list1:", 5 not in list1)

print("\nIdentity Operators:")
m = [1, 2]
n = [1, 2]
print("m is n:", m is n)          # False (different objects)
print("m is not n:", m is not n)  # True
