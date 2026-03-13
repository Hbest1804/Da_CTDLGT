class Solution(object):
    def sumOfUnique(self, nums):
        return sum(n for n in nums if nums.count(n)==1)
        