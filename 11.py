a = [int(s) for s in input().split()]
mx = a[0]
mi = 0
for i in range(1, len(a)):
    if a[i] > mx:
        mx = a[i]
        mi = i
print(mx, mi)
