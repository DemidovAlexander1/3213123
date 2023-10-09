a = int(input())
b = int(input())
if a > b:
    max1 = a
    max2 = b
else:
    max1 = b
    max2 = a
while b != 0:
    b = int(input())
    if b > max1:
        max2 = max1
        max1 = b
    elif b > max2:
        max2 = b
print(max2)