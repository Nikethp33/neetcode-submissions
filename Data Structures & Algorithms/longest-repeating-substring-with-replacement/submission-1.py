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

            while (len(window) - maxfreq > k):
                ele  = s[l]
                window.remove(s[l])
                l += 1
                dic[ele] = dic.get(ele) - 1

            if len(window) - maxfreq <= k:
                length = max(length,len(window))
        
        return length
            

                

            