a = [int(i) for i in input().split()]
k, c = [int(e) for e in input().split()]
a.insert(k, c)
a = (" ".join([str(i) for i in a]))
print(a)