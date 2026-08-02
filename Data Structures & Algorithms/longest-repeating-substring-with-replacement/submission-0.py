class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        window = []
        dic = {}
        maxfreq = 0
        length = 0

        for r in range(len(s)):
            dic[s[r]] = dic.get(s[r], 0) + 1
            window.append(s[r])
            maxfreq = max(maxfreq,max(list(dic.values())))

            if len(window) - maxfreq <= k:
                length = max(length,len(window))
 
            while (len(window) - maxfreq > k):
                ele  = window.pop(0)
                l += 1
                dic[ele] = dic.get(ele) - 1
        
        return length
            

                

            