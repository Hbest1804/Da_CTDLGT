class Solution(object):
    def largestAltitude(self, gain):
        a = 0
        max_a=0
        for g in gain:
            a +=g
            max_a=max(max_a,a)
        return max_a
        