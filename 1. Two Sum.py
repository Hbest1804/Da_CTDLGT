class Solution:
    def twoSum(self, nums, target):
        mp = {}
        
        for i in range(len(nums)):
            needs = target - nums[i]
            
            if needs in mp:
                return [mp[needs], i]
            
            mp[nums[i]] = i
        
        return []