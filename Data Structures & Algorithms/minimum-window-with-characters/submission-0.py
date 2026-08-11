class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
                
        for i in t:
            need[i] = need.get(i,0) + 1
        l = 0
        have = 0
        need_cnt = len(need)
        res = ""
        reslen = float("inf")
        
        for r in range(len(s)):
            c = s[r]
            if c in need:
                window[c] = window.get(c,0) + 1

                if window[c] == need[c]:
                    have += 1

            while have == need_cnt:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = s[l:r+1]

                lc = s[l]

                if lc in need:
                    window[lc] -= 1
                    if window[lc] < need[lc]:
                        have -= 1
                    
                l += 1
        return res
                 


                

                    



