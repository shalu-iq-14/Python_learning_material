# choice()
# choices()
# randint()
# randrange()
# sample()
# shuffle()




import random
emp_name=["aman","kamal","shivam","anshu"]
weight=[2,3,1,0]
res=random.choices(emp_name,weights=weight, k=4)
print(res)

import random
res=random.random()*10000
print(int(res))



import random
rand_int=random.randint(1,10)      
rand_range=random.randrange(1,10)

print(rand_int)
print(rand_range)


# user max attempt =6
# each attempt random number generate
# random number generate sum
# fix_value  = 150


import random
attempt=6
total = 0
fix_value=150

for i in range(1, attempt + 1):
    num = random.randint(1,50)
    total+=num

    print(f"attempt {i}: ramdom number = {num}, total sum {total}")

    if total >= fix_value:
        print("targate reached : sum = {total}")
        break

    elif total < fix_value and total > 140:
        print(f"you are too close : sum = {total}")

else:
    print(f"you are too far : sum= {total}")



# sample()
import random
emp_name=["aman","kamal","shivam","anshu"]
res = random.sample(emp_name, k=2)
print(res)


# shuffle()
import random
emp_name=["aman","kamal","shivam","anshu"]
random.shuffle(emp_name)
print(emp_name)

# generate 10 coupon code
# --->cxyc2345

import random
def generate_coupon():
    A_TO_Z  ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    NUM="1234567890"

    char=[random.choice(A_TO_Z)for i in range(1,5)]
    number=[random.choice(NUM)for i in range(1,5)]
    print("".join(char+number))

for i in range(1,10):
    generate_coupon()



import random
def generate_coupon():
    A_TO_Z  ="abcdefghijklmnopqrstuvwxyz"
    num="1234567890"

    char="".join(random.choices(A_TO_Z, k=4))
    num=random.random()*10000
    res=char.upper()+str(int(num))
    print(res)

for i in range(1,10):
    generate_coupon()



import random
def generate_coupon():
    import string
    print(string.ascii_letters)
    print(string.digits)
for i in range(1,10):
    generate_coupon()




import random
def generate_coupon():
    import string
    "".join(random.choices(string.ascii_uppercase , k=4))
    +"".join(random.choices(string.digits , k=4))
for i in range(10):
    generate_coupon()





