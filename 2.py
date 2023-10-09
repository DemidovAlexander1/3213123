n = int(input())
m = 1
i = 0
while m <= n:
    if m == n:
        print(i)
        break
    else:
        m = m * 2
        i = i + 1
if m > n:
    print("No")
