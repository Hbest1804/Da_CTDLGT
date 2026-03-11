class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        words = re.findall(r'\w+',paragraph)
        banned = set(banned)
        count = Counter()
        for word in words:
            if word not in banned:
                count [word] +=1 
        return count.most_common(1)[0][0]
        