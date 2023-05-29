a=[1,2,3,4,5]
print(a)
b=["hello","world"]
print(b)
c=["hello",1,2,"world"]
print(c)
print(c[1])
print(c[-1])
print(c[-2])
print(c[-3])
print(c[-4])
if 1 in c:
    print("1 is present")
else:
    print("not present")
print(c[1:3])
print(c[0:3+1:2])
c.append("yes")

colors = ["voilet", "indigo", "blue"]
print(colors)
colors.append("green")
print(colors)
colors.insert(1,"white")
print(colors)
colors.extend(c)
print(colors)
print(colors+a)

print(a)
a.pop()
print(a)
a.pop(0)
print(a)

a.remove(3)
print(a)

del a[1]
print(a)

#del a
print(a)

a.clear()
print(a)