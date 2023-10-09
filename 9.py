n = input().split()
chet = []
for i in range(len(n)):
    n[i] = int(n[i])
    # print(n[i])
    if (i - 1) % 2 != 0:
        chet.append(str(n[i]))
print(' '.join(chet))
