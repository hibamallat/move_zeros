"""
Write a function move_zeros(numbers) that moves all 0s to the end 
of the list while maintaining the order of the other elements.
"""

def move_zeros(numbers):
    # Create two separate lists: one for non-zero numbers and one for zeros
    zeros_list= []
    non_zeros_list= []

    for i in range(len(numbers)):
        
        if numbers[i] == 0:
            zeros_list.append(numbers[i])
        else:
            non_zeros_list.append(numbers[i])

    # Combine the non-zero list and the zeros list (zeros at the end)
    return non_zeros_list + zeros_list

list_nums = []
try:
    size = int(input("How many numbers would you like to add to the list? "))

    for i in range (size):
        # Collect user numbers and add them to list_nums
        user_num = int(input(f"Please enter a number {i + 1}: "))
        list_nums.append(user_num)

    print(f"The original list: {list_nums}")
    move_zeros_list = move_zeros(list_nums)
    print(f"After moving zeros list: {move_zeros_list}")

except ValueError:
    print("Enter a number!")
