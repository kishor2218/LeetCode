class Solution(object):
    def twoSum(self, nums, target):
        arr=[0,0]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    arr[0]=i
                    arr[1]=j
                    return arr
        return arr
       
