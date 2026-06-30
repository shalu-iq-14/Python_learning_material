#-------- file handling
# 1. file handling in python means reading from and writing to files/folder stored on 
# disk using python.

# 2. your python code can open a file, pull out data of it, put data into it and also
# close it properly.


# --------- what is file
# files are store of data and information on the specific path of device.

# types of file----
# 1. text file(.txt, .csv, .json)
# 2. binary file (images, vedios, audio)


# types of file path---
# 1. absoulte path : the complete path from the root of the filesystem.
# 2. relative path : the path relative to where your current folder(current working dir)


# file mode
# 1. a: appened, a+ : append and read
# 2. w: write, w+ : write and read
# 3. r: read, r+ : read and write
# 4. x: strictly create file


# python file handling methods---
# 1. open(file_name, mode) : opens file
# 2. close(): close file.
# 3. flush(): memory cleanup.


# 4. read(): file read
# 5. readlines(): file read line by line
# 6. write(): writes data in file only take string
# 7. writeline(): write data in file of any data type.


# 8. tail(): cursor move.
# 9. seek() : specific position set of cursor.


# # 1. create a file in strict mode.
file = open('strict.txt', 'x')
print("file created...")

file=open('write.txt', 'w')
file.write("this id python file handling")
print("file created...")



file=open('write.txt', 'w')
file.write("this id python file handling")
file.flush()
file.close()
print("file created...")


# context manager
# with open(filename, mode) as file:

with open('manager', 'w+') as file:
    file.write("this is completely python file handling....")
    file.seek(0)
    r=file.read()
    print(f"file content: {r}")


# wap file name demo.txt 
with open('demo.txt','r') as file:
    r=file.read()
new_file=""
for ch in r:
    if not ch.isdigit():
        new_file=new_file+ch

with open('new_demo.txt','w') as file:
        file.write(new_file)



emp_list = ["aman","shivam","shubham","anshu","kamal"]
# emp name individual file create text type

file=open('aman.txt', 'w')
file.write("this id python file handling")
print("file created...")


file=open('shivam.txt', 'w')
file.write("this id python file handling")
print("file created...")


file=open('kamal.txt', 'w')
file.write("this id python file handling")
print("file created...")

file=open('shubham.txt', 'w')
file.write("this id python file handling")
print("file created...")


file=open('anshu.txt', 'w')
file.write("this id python file handling")
print("file created...")

emp_list = ["rohit","prateek","kavita","anshul","jyoti"]
for i in emp_list:
    with open(f"{i}.txt","w") as file:
        print(f"{i}.txt file created...")
    
