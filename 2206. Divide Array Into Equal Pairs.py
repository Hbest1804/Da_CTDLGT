class Solution(object):
    def divideArray(self, nums):
        count = Counter(nums)
        for value in count.values():
            if value % 2 !=0:
                return False
        return True

        