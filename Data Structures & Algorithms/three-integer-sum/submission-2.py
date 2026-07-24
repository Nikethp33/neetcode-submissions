class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        res = []
        
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            while j < k:
                if nums[j] + nums[k] > -(nums[i]):
                        k -= 1
                
                elif nums[j] + nums[k] < -(nums[i]):
                        j += 1
            
                elif nums[j] + nums[k] + nums[i] == 0:
                    if [nums[i],nums[j],nums[k]] not in res:
                        res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1


        
        return res

                

