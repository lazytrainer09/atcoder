import math

a, b, d = map(int, input().split())

rad = math.pi * d / 180

a1 = a * math.cos(rad) - b * math.sin(rad)
b1 = a * math.sin(rad) + b * math.cos(rad)

print(a1, b1)
