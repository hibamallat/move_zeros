list_nums=[1,0,4,0,3,2]
zero_list=[]

def move_zeros(numbers):
    for i in numbers:
        if i == 0:
            zero_list.append(i)
            list_nums.remove(i)

    return list_nums + zero_list

print("The original list:",list_nums)
update_list = move_zeros(list_nums)
print("After moving zeros list:",update_list)
