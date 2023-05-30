a="hello world"
b="uNiverSe"
print(a.count("o"))
print(a.index("w"))

print(a.swapcase())
print(b.swapcase())
print(b.upper())
print(b.lower())

dict={"1":5,"2":6}
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print("sorted values : ",sorted(dict.values()))
print("reverse sorted keys : ",sorted(dict.keys(),reverse=True))

print("sorted items : ",sorted(dict.items()))
print("reverse sorted items : ",sorted(dict.items(),reverse=True))
d=sorted(dict.items(),reverse=True)
print(d)


