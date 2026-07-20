class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        def merge_sort(nums):
            # Base case
            if len(nums) <= 1:
                return

            # Split the array
            mid = len(nums) // 2
            left_half = nums[:mid]
            right_half = nums[mid:]

            # Recursively sort both halves
            merge_sort(left_half)
            merge_sort(right_half)

            # Merge the sorted halves
            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] <= right_half[j]:
                    nums[k] = left_half[i]
                    i += 1
                else:
                    nums[k] = right_half[j]
                    j += 1
                k += 1

            # Copy remaining elements from left half
            while i < len(left_half):
                nums[k] = left_half[i]
                i += 1
                k += 1

            # Copy remaining elements from right half
            while j < len(right_half):
                nums[k] = right_half[j]
                j += 1
                k += 1

        # Sort the array
        merge_sort(nums)

        # Check adjacent elements for duplicates
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        return False