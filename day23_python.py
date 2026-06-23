str1=[22,43,65,87]
even=[]
odd=[]
for i in str1:
    if i % 2==0:
        even.append(i)
    else:
        odd.append(i)
print("even_num",even, "odd_num", odd)


str1="456 this-is-python 123"
for i in str1.split():
    if i.isdigit():
        print(i)


str1="456this-is-python 123"
count=0
for i in str1:
    if i.isdigit():
        count+=1
print(count)


str1="this is python"
vowel="aeiouAEIOU"
for i in range(len(str1)):
    if str1 [i] in vowel:
        print(i, str1[i])



str1="this is python"
vowel="aeiouAEIOU"
for i in str1:
    if i not in vowel:
        print(i)


str1="python"
for i in range(len(str1)):
    print(str1[i],i)


str1=["python programming"]
for i in str1:
    for j in i:
        if j == "h" or j == "m":
            continue
        print(j,end="")



n1= 3
n2= 5
n3=7
if n1>n2 and n1>n3:
    print("n1 is greater",n1)
elif n2>n1 and n2>n3:
    print("n2 is greater",n2)
else:
    print("n3 is greater",n3)



str1=["python programming"]
for i in str1:
    print(i[::-1])

