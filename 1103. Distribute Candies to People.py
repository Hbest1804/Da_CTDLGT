class Solution(object):
    def distributeCandies(self, candies, num_people):
        result = [0]*num_people
        give =1
        i =0
        while candies >0:
            idx = i %num_people
            if candies >= give:
                result [idx] +=give
                candies -= give
            else:
                result [idx] +=candies
                candies =0
            give +=1
            i +=1

        return result