class Solution:

    def search(self, nums: List[int], target: int) -> int:
        
        def bs(low, high):
            if low > high:
                return -1

            mid = (high+low) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                return bs(mid + 1,high)
            
            elif nums[mid] > target:
                return bs(low, mid - 1)
            
        return bs(0, len(nums)-1)
        

            
            