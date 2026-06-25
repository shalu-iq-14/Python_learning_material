#  -------------------SET------------------------------------
# defination and property of set.
# --------------DEFINATION------------------------
# ---> set is a data structure IN PYTHON used to store unique values in {} braces.
# ---> unordered, mutable
# ---> sets does not supports indexing, slicing, sequence
# ---> value can be any type of data(hetrogenous and homogenous).
# ---> sets always recnize unique values


# --------------CREATION OF SETS------------------------
empty_set=set()
days={"monday","tuesday","wednesday","thrusday","friday"}
print(type(days))
print(days)


# traversing
for i in "days":
    print(i)



# in-built methods
# add()
# intersect()
# difference()
# subset()
# superset()
# union()

# adding
my_set={1,3,4,5,6}
my_set.add(9)
print(my_set)


# removing
my_set={1,2,3,4,5,6}
my_set.remove(3)
print(my_set)


# intersecting
num1={1,2,3,4,5}
num2={4,5,6,7,8}
intersect_set=num1.intersection(num2)
print(intersect_set)


# difference
num1={1,2,3,4,5,6}
num2={5,6,7,8,9,10}
difference_num=num1.difference(num2)
print(difference_num)


# subset()
set1={1,2,3,4,5,6}
set2={1,2,3}
print(set2.issubset(set1))
print(set1.issubset(set2))


# superset()
set1={1,2,3,4,5,6}
set2={1,2,3}
print(set2.issuperset(set1))
print(set1.issuperset(set2))


# union
num1={1,2,3,4,5}
num2={4,5,6,7,8}
union_num=num1.union(num2)
print(union_num)