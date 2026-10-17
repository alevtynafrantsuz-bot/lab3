a = int(input())
b = int(input())

q = 0
r = a

while r >= b:
    r = r - b
    q = q + 1

print(q, r)