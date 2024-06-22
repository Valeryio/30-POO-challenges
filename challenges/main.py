#!/usr/bin/env python3

from vector_4d import Vector4D as Vector

a = Vector(1, 2, 3, 4)

b = a + a

print(b)
c = Vector(1, 1, 1, 1)
print(b - c)
