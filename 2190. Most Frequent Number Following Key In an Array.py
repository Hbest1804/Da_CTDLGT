class Solution(object):
    def mostFrequent(self, nums, key):
        arr =[]
        for i in range(len(nums)-1):
            if nums[i]==key:
                arr.append(nums[i+1])
        return Counter(arr).most_common(1)[0][0]
            


        