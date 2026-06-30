import os
# print(os.listdir())

print(os.getcwd())

emp_list = ["aman","shivam","shubham","anshu","kamal","xyz","shalu"]
for i in emp_list:
    file_check= os.path.exists(f"{i}.txt")
    if not file_check:
        with open(f"{i}.txt","w") as file:
            print(f"{i}.txt file created")
    else:
        print(f"{i}- file already exists")

import os
emp_list = ["aman","shivam","shubham","anshu","kamal"]
for i in emp_list:
    os.remove(f"{i}.txt")
    print(i, "removed...")


import os

path = r"C:\Users\HP\Desktop\pythonclasscode"
os.chdir(path)

dir_name = "employee_details"

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

emp_list = ["aman", "shivam", "shubham", "anshu", "kamal"]

for emp in emp_list:
    file_path = os.path.join(dir_name, f"{emp}.txt")

    with open(file_path, "w") as file:
        file.write(f"Employee Name: {emp}")

print("All files created successfully.")



import os
dir_name="students_details"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

stu_name=["samyak","abhi","mani","rohan","sumit"]
for stu in stu_name:
    file_path= os.path.join(dir_name,f"{stu}.txt")
    with open(file_path,'w') as file:
        file.write(f"student details : {stu}")

print("all file created successfully")