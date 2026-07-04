def max_num(nums):
    max_num=0
    for num in nums:
        if num>max_num:
            max_num=num
    return max_num
print(max_num([2,3,1,5,1,7,23,1,0,56]))
