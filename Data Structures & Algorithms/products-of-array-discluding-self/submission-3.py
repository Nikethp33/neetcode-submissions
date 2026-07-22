class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        count = 0
        for i in nums:
            if i != 0:
                product = 1
                break
            else:
                product = 0
        
        
        for i in nums:
            if i == 0:
                continue
            product *= i
        

        if 0 in nums:
            for i in nums:
                if i == 0:
                    count += 1

            for i in nums:    
                if i == 0:
                    if count > 1:
                        output.append(0)
                    else:
                        output.append(int(product))
                else:
                    output.append(0)
        else:

            for i in nums:
                output.append(int(product/i))
            
        
        return output
        
