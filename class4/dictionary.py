a = {1: 25, 3: 10, 2: 35}
print("ascending order : ", dict(sorted(a.items())))

b=sorted(a.items(), reverse=True)
print(b)
c=dict(b)
print(c)
print(list(c.items()))