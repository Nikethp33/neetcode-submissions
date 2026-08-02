class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d1 = {}
        d2 = {}

        
        for c in s1:
            d1[c] = d1.get(c, 0) + 1


        for i in range(len(s1)):
            d2[s2[i]] = d2.get(s2[i], 0) + 1

        if d1 == d2:
            return True

        l = 0
        for r in range(len(s1), len(s2)):

            d2[s2[r]] = d2.get(s2[r], 0) + 1


            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]]

            l += 1

            if d1 == d2:
                return True

        return False