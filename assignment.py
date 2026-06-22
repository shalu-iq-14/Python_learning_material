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


