class Solution(object):
    def minimumSum(self, num):
        """
        :type num: int
        :rtype: int
        """
        digist=[int(d) for d in str(num)]
        digist.sort()
        num1 = digist[0]*10 +digist[2]
        num2 = digist[1]*10 +digist[3]
        return num1 +num2

        