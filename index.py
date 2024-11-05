list_nums=[]
zero_list=[]

def move_zeros(numbers):
    for i in numbers:
        if i == 0:
            zero_list.append(i)
            list_nums.remove(i)

    return list_nums + zero_list

for i in range (8):
    user_num = int(input("Please enter a number: "))
    list_nums.append(user_num)

    if user_num == -1:
        list_nums.remove(user_num)
        break


print("The original list:",list_nums)
update_list = move_zeros(list_nums)
print("After moving zeros list:",update_list)
