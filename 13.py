a = [1, 2, 5, 0, 7, 3, 2]
print(a)

for i in range(0, len(a) - 1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]

print(a)
