print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")

def get_user_input():
    num_list = input("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    num_list = num_list.split(",")
    nums = [float(i) for i in num_list]
    return nums

def calc_average_temperature(nums):
    sum = 0
    for i in nums:
        sum = sum + i
    avg = sum / len(nums)
    print(str(avg))

def calc_min_max_temperature(nums):
    nums2 = nums.copy()
    while(len(nums) > 1):
        i = 0
        if(nums[i] > nums[i+1]):
            del nums[i+1]
        elif(nums[i] <= nums[i+1]):
            del nums[i]
        max_temperature = nums[0]

    while(len(nums2) > 1):
        i = 0
        if(nums2[i] > nums2[i+1]):
            del nums2[i]
        elif(nums2[i] <= nums2[i+1]):
            del nums2[i+1]
        min_temperature = nums2[0]

    print("The max temperature is " + str(nums[0]))
    print("The min temperature is " + str(nums2[0]))






calc_min_max_temperature(get_user_input())