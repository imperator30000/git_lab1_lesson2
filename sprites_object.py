s = 11
e = 2
for i in range(e - 1):
    print(s, i)
    s += 4 + i % 2
print(s)