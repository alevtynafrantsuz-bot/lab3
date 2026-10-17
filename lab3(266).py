n = int(input())

maximum = 0
minimum = 301
count = 0

for i in range(n):
    v = int(input())
    if v > maximum:
        maximum = v
    if v < minimum:
        minimum = v
    if v <= 30:
        count += 1

print(maximum - minimum, count)
