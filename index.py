"""
Write a function move_zeros(numbers) that moves all 0s to the end 
of the list while maintaining the order of the other elements.
"""

def move_zeros(numbers):
    zeros_list=[]
    non_zeros_list=[]

    for i in range(len(numbers)):
        
        if numbers[i] == 0:
            zeros_list.append(numbers[i])
        else:
            non_zeros_list.append(numbers[i])

    return non_zeros_list + zeros_list

list_nums=[]

print("Enter -1 to stop")

for i in range (8):

    user_num = int(input("Please enter a number: "))
    list_nums.append(user_num)

    if user_num == -1:
        list_nums.remove(user_num)
        break

print("The original list:",list_nums)
zeros_right_list = move_zeros(list_nums)
print("After moving zeros list:",zeros_right_list)
