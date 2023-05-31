countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

"""Unpacking is the process of assigning 
the tuple items as values to variables"""

info = ("Arun", 20, "KTU")
(name, age, university) = info
print("Name:", name)
print("Age:",age)
print("Studies at:",university)

"""
Sets are unordered collection of data items. They store multiple items in a single variable. 
Sets items are separated by commas and enclosed within curly brackets {}.
 Sets are unchangeable, meaning you cannot change items of the set once created. 
 Sets do not contain duplicate items
"""

info = {"tinu", 19, False, 5.9}
for item in info:
    print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)

"""
The main difference between remove and discard is that, if we try to delete an item 
which is not present in set, then remove() raises an error, whereas discard() does 
not raise any error
"""
cities.remove("Tokyo")
print(cities)
cities.discard("Mandrid")
print(cities)
"""
pop():
This method removes the last item of the set but the catch 
is that we don’t know which item gets popped as sets are unordered. 
However, you can access the popped item if you assign the pop() method to a variable
"""
item = cities.pop()
print(cities)
print(item)

cities.clear()
print(cities) #This method clears all items in the set and prints an empty set."""
del cities #del is not a method, rather it is a keyword which deletes the set entirely"""

info = {"Carla", 19, False, 5.9}
if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")

"""
union() and update():
The union() and update() methods prints all items that are present in the two sets. The union() method returns a new set whereas update() method adds 
item into the existing set from another set
"""
cities={"egypt","losvegas"}
cities21={"mavelikkara","mannar","kayamakulam"}
cities22={"alleppey","ekm"}
cities3 = cities.union(cities21)
print(cities3)
cities3.update(cities22)
print(cities3)

"""The intersection() and intersection_update() methods prints only items that are similar 
to both the sets. The intersection() method returns a new set whereas intersection_update() method updates 
into the existing set from another set."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

"""The symmetric_difference() and symmetric_difference_update() methods prints only items that are not 
similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() 
method updates into the existing set from another set."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

"""The difference() and difference_update() methods prints only items that are only present
in the original set and not in both the sets. The difference() method returns a new set whereas difference_update()
method updates into the existing set from another set."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)

"""The isdisjoint() method checks if items of given set are present in another set. 
This method returns False if items are present, else it returns True."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))


"""he issuperset() method checks if all the items of a particular set are present in the original set.
It returns True if all the items are present, else it returns False."""
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Seoul", "Madrid","Kabul"}
print(cities.issuperset(cities3))

""""pip stands for Package Installer for Python. 
It  is used to install and manage software packages in python that are not the part of standard python library.

In the later versions of python (3.4 and after), the pip command is pre-installed.
pip --version
pip install numpy
pip install sklearn
pip list
kklecturenotes@gmail.com
"""
