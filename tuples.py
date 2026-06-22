# -------------------TUPLES------------------------------------
# defination and property of tuple.
# --------------DEFINATION------------------------
# ---> tuple is a data structure IN PYTHON used to store multiple data of 
# different types with comma(,) in round brackets ().
# immutable
# support indexing and slicing and ordered

# --------------CREATION OF TUPLE------------------------
t1=(50,40,30,)
print(type(t1))


t1,t2,t3=(50,40,"jain")
print(type(t3))
print(t1)
print(t2)
print(t3)


# indexing and slicing in tuple
marks_tuple=(50,40,30,20,10)
print(marks_tuple[0])
print(marks_tuple[1:4])


# mutability
# marks_tuple=(50,40,30,20,10)
# marks_tuple[0]=100
# print(marks_tuple)


# traversing in tuple
def tuple_fun(m):
    new_value=[]
    for i in m:
        if i >= 50:
            new_value.append(i)
    return new_value
marks_tuple=(50,40,55,70,100,87,33,66)
res=tuple_fun(marks_tuple)
print(res)


# 2.waf to sum of indices of tuple
def sum_tuple(t):
    count=0
    for i in t:
        count+=i
    return count

marks_tuple=(50,40,55,70,100,87,33,66)
res=sum_tuple(marks_tuple)
print(res)



marks_tuple=(50,40,55,70,100,87,33,66)
s=0
for i in range(len(marks_tuple)):
    s+=i
print(s)