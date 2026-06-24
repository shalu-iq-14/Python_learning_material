# -------------------DICTIONARY------------------------------------
# defination and property of dictionary.
# --------------DEFINATION------------------------
# ---> dictionary is a data structure IN PYTHON used to store multiple data in key:value formate.
# ---> ordered, mutable
# ---> indexed by key, not position
# ---> key must be unique (immutable)
# ---> value can be any type of data.
# ---> used in fast lookup


# --------------CREATION OF TUPLE------------------------
stu_profile={"aman":"noida", "rohan":"delhi"}
print(type(stu_profile))
print(stu_profile)


stu_marks=dict([("aman",300),("shivam",80)])
print(stu_marks)


stu_profile={"aman":"noida", "rohan":"delhi"}
stu_profile["aman"]="morena"
print(stu_profile)


# --------------traversing------------
# stu_marks={"aman":300, "shivam":80, "abhi":44}


# ------inbuilt method------------
stu_marks={"aman":300, "shivam":80, "abhi":44}
v=stu_marks.values()
print(v)


stu_marks={"aman":300, "shivam":80, "abhi":44}
k=stu_marks.keys()
print(k)


stu_marks={"aman":300, "shivam":80, "abhi":44}
i=stu_marks.items()
print(i)


stu_marks={"aman":300, "shivam":80, "abhi":44}
g=stu_marks.get("rohan","not found")
print(g)


# --------- update()-------
stu_marks={"aman":300, "shivam":80, "abhi":44}
stu_marks_new={"komal":200, "monisha":250}
stu_marks.update(stu_marks_new)
print(stu_marks)



profile={"aman":{
    "address":["noida","delhi","mumbai"]},
    "shalu":{"addres":["morena","gwalior","delhi"]}
}
res=profile["aman"]
print(res)


profile={"aman":{
    "address":["noida","delhi","mumbai"],
    "hobbbies":["reading","cooking","travelling"],
    "password":{"insta":4354, "fb":76589}
    },
    "shalu":{"addres":["morena","gwalior","delhi"]}
}
res=profile.get("aman")
print(res)






profile={"aman":{
    "address":["noida","delhi","mumbai"],
    "hobbbies":["reading","cooking","travelling"],
    "password":{"insta":4354, "fb":76589}
    },
    "shalu":{"addres":["morena","gwalior","delhi"]}
}
res=profile["aman"]["password"]
print(res)



profile={"aman":{
    "address":["noida","delhi","mumbai"],
    "hobbbies":["reading","cooking","travelling"],
    "password":{"insta":4354, "fb":76589}
    },
    "shalu":{
        "addres":["morena","gwalior","delhi"],
        "hobbies":["reading","painting","travelling"],
        "password":{"insta":7678, "fb":8669}},
}
res=profile["aman"]["password"]["insta"]
print(res)