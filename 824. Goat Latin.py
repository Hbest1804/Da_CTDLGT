class Solution(object):
    def toGoatLatin(self, sentence):
        vowels = set("aeiouAEIOU")
        words = sentence.split()
        res = []
        for i , word in enumerate(words , start=1):
            if word[0] in vowels:
                new_word = word
            else:
                new_word = word[1:] + word[0]
            new_word += "ma" +("a"*i)
            res.append(new_word)
        return " ".join(res)
        