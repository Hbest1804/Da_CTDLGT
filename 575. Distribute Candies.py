class Solution(object):
    def distributeCandies(self, candyType):
        unique_type=len(set(candyType))
        max_eat=len(candyType)//2
        return min(unique_type,max_eat)
        