from vector import *

# homework: add v4, v5, add two comparison between those.
v1 = Vector(3, 4)
v2 = Vector(2, 2)
v3 = Vector(3, 4)
v4 = Vector(5, 6)
v5 = Vector(1, 1)
print(v1 == v2)
print(v1 == v3)
print(abs(v1))
print(abs(v2))
print(v1 < v2)
print(v1 > v2)
print()

print(v4 == v5)
print(v4 == v4)
print(abs(v4))
print(v4 < v5)

print(v4 / 4)

print('Vector 1:', v1)
print('Vector 2:', v2)
print('Vector 1 + Vector 2:', v1 + v2)
print('Vector 1 - Vector 2:', v1 - v2)
print('Vector 1 times Vector 2:', v1 * v2)
print('Vector 1 times 5:', v1 * 5)
