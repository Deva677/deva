# set methods
a={1,2,3,4,5,5,6,6,677}
print(type(a))
a.add(234)
print(a)
a.remove(677)
print(a)
a.pop()
print(a)
a.update({1,2,3,4,4,4,4,4,3,})
print(a)

# set operaters
# union
set1={1,2,3,4}
set2={7,8,9,0}
print(set1.union(set2))

# intersection
set1={1,2,3,4}
set2={7,8,9,4}
print(set1.intersection(set2))

# difference
set1={2,3,4,5,6}
set2={9,8,7,6,5,3}
print(set1.difference(set2))

# issubset
set1={1,2,3,4,5,6,7}
set2={1,2,3,4,5,6}
print(set1.issubset(set2))

# issuperset
set1={2,3,4,5,6,7}
set2={2,3,4,5,6}
print(set1.issuperset(set2))

# tuple methods
tuple1=(1,2,3,4,5,6)
print(type(tuple1))