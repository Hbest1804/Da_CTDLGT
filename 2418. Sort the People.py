class Solution(object):
    def sortPeople(self, names, heights):
        p = zip(heights,names)
        p = sorted(p,reverse=True)
        return [name for height, name in p]