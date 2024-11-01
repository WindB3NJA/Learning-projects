nums = [3,2,4,3]
target = 6
counter = 0
list = []

for index_frist_num, frist_num in enumerate(nums):
    for index_second_num , second_num in enumerate(nums):
        sum = frist_num + second_num
        if index_frist_num != index_second_num:
            if sum == target:
                if index_frist_num or index_second_num not in list:
                        list.append(index_frist_num)

print(list)