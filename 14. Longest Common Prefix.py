class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None or len(strs) == 0:
            return ""
        
        pre = strs[0]
        
        for i in range(1, len(strs)):
            while not strs[i].startswith(pre):
                pre = pre[:-1]  
                if pre == "":
                    return ""
        
        return pre