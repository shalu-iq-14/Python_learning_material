#1. Write a Python program to find the sum of all elements in the list [10, 20, 30, 40, 50]

def lst_sum(num):

    return sum(num)
element=[10, 20, 30, 40, 50]
print(lst_sum(element))

# 2.Write a Python program to display the odd and even elements from the list [10, 23, 11, 12, 33, 44, 2, 5, 6]
def display_num(num):
    even=[]
    odd=[]
    for i in num:
        if i % 2 ==0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd

numbers=[10,23, 11, 12, 33, 44, 2, 5, 6]
even, odd = display_num(numbers)
print("Even elements:", even)
print("Odd elements:", odd)



# 3. Write a Python program to count the odd and even numbers in the list [10, 23,
# 11, 12, 33, 44, 2, 5, 6].
def number_list(num):
    even=[]
    odd=[]
    for i in num:
        if i % 2==0:
            even.append(i)
        else:
            odd.append(i)
    return even, odd
    
numbers=[10,23, 11, 12, 33, 44, 2, 5, 6]
even, odd = number_list(numbers)
print("Even elements:", even)
print("count the even number:",(len(even)))
print("Odd elements:", odd)
print("count the odd number:",(len(odd)))


# 4.Write a Python program to interchange the first and last elements in the list [10,
# 23, 11, 12, 33, 44, 2, 5, 6].
def interchange(num):
    first_ele=element[0]
    last_ele=element[-1]
    element[0]=last_ele
    element[-1]=first_ele

    return num

element=[10,23, 11, 12, 33, 44, 2, 5, 6]
interchange(element)
print("List after interchange:", element)



# 5. Write a Python program to duplicate all the items in the list li = [1, 2, 3],
# such that the result is:
# output = [1, 2, 3, 1, 2, 3, 1, 2, 3].
def double(num):
    return num * 3

num=[1, 2, 3]
print(double(num))



# 6. Find the smallest element in the list [10, 23, 11, 12, 33, 44, 2, 5, 6]
def smallest(num):
    return min(num)

smallest_element=[10, 23, 11, 12, 33, 44, 2, 5, 6]
print("Smallest element in the list:", smallest(smallest_element))


# 7. Find the greatest element in the list [89, 23, 24, 2, 55, 54, 64]
def greatest(num):
    return max(num)

greatest_element=[89, 23, 24, 2, 55, 54, 64]
print("Greatest element in the list:", greatest(greatest_element))  


# 8. Find the repetitive elements in the list [1,2,3,4,56,1,22,23,33,23, 56].
def repetitive(num):
    repeated=[]