class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # Variables
        l = 0
        r = len(numbers) 

        # Store in Hash Set
        while l < r:
            if numbers[l] + numbers[r - 1] > target:
                r -= 1
            elif numbers[l] + numbers[r - 1] < target:
                l += 1
            else:
                return [l + 1, r]

            


        # Loop through, do target - current index

        # Find if remaining value exists
        # If true, return index for curr and remaining + 1
        