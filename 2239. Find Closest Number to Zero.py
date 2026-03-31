class Solution(object):
    def findClosestNumber(self, nums):
        closets = nums[0]
        for num in nums:
            if abs(num)<abs(closets):
                closets = num
            elif abs(num)==abs(closets) and num > closets:
                closets = num
        return closets


        