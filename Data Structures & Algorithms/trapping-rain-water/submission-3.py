class Solution:
    def trap(self, height: List[int]) -> int:
        dic = {}
        if len(height)==0:
            return 0
        prefix_max = height[0]
        suffix_max = height[len(height)-1]
        water = 0

        for i in range(len(height)):
            if height[i] >= prefix_max:
                prefix_max = height[i] 
            dic[i] = [prefix_max]  

        for i in range(len(height)-1,-1,-1):
            if height[i] >= suffix_max:
                suffix_max = height[i]   
            dic[i].append(suffix_max)   
    
        for i in range(1,len(height)-1):
            water += min(dic[i][0],dic[i][1]) - height[i]
    
        return water
