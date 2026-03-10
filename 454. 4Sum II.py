class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        countAB ={}
        for a in nums1:
            for b in nums2:
                s=a+b
                countAB[s]=countAB.get(s,0)+1
        result=0
        for c in nums3:
            for d in nums4:
                target =-(c+d)
                if target in countAB:
                    result+=countAB[target]
        return result
        