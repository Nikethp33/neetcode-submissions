class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ele = []
        count = 0
        maxlen = 0

        for i in range(len(s)):
            ele.append(s[i])
            count += 1
            for j in range(i+1,len(s)):
                if s[j] not in ele:
                    count += 1
                    ele.append(s[j])
                else:
                    break
            maxlen = max(count, maxlen)
            ele.clear()
            count = 0

        return maxlen    