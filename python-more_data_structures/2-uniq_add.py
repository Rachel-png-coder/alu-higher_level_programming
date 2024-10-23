#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_nums = set()
    sum_unique = 0
    for num in my_list:
        if num not in unique_nums:
            sum_unique += num
            unique_nums.add(num)
    return sum_unique
