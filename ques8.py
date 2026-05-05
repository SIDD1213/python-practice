#Maximum element in array
def find_max(arr):
    max_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element=num

    return max_element
arr=[2,4,6,9]
print(find_max(arr))

class solution:
    def findmax(self,nums):
        max_element=num[0]
        for n in nums:
            if n>max_element:
                max_element=n
        return max_element

