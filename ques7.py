#Minimum in Rotated Sorted Array

def findMin(nums):
    len=0
    right =len(nums)-1

    while left<=right:
        mid=(left+right)//2

        if nums[mid]>nums[right]:
            left=mid+1
        else:
            right=mid
        return nums[left]