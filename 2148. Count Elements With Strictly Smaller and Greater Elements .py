class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_nums = min(nums)
        max_nums = max(nums)
        count = 0
        for num in nums:
            if num>min_nums and num<max_nums:
                count +=1
        return count
        