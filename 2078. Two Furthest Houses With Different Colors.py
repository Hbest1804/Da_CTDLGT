class Solution(object):
    def maxDistance(self, colors):
        max_dist = 0
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i] != colors[j]:
                    max_dist = max(max_dist,j-i)
        return max_dist
        