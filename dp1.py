# 1. Write a Python program to sort a list in ascending order without using the sort() method.
def asc_list(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                c = nums[i]
                nums[i] = nums[j]
                nums[j] = c
    return nums

nums= list(map(int,input("ENter elements:").split()))
print(asc_list(nums))



# 2. Write a program to find the maximum number in a list without using max() or min().

def max_num(nums):
    maxi = nums[0]
    for i in range(0,len(nums)):
        if maxi < nums[i]:
            maxi = nums[i]
    return maxi

nums = list(map(int,input("ENter Elements:").split()))
print(max_num(nums))




# 3. Write a Python program to find the second largest number in a list without using sort().

def sec_lar(nums):
    fmax = float('-inf')
    smax = float('-inf')
    for i in range(0,len(nums)):
        if nums[i] > fmax:
            smax = fmax
            fmax = nums[i]
        elif nums[i] > smax and nums[i] != fmax:
            smax = nums[i]
    return smax

nums = list(map(int,input("Enter elements:").split()))
print(sec_lar(nums))