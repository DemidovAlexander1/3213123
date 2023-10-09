a = [{min(a): max(a), max(a): min(a)}.get(x, x) for x in a]

# 15
a = [7, 6, 5, 4, 3, 2, 1]
k = 2
result = a[:k] + a[k + 1:]
print(result)