class Solution(object):
    def duplicateZeros(self, arr):
        result =[]
        for x in arr:
            result.append(x)
            if x==0 :
                result.append(0)
        for i in range (len(arr)):
            arr[i]=result[i]