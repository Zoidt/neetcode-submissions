class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for i in range(len(nums)):
        #     # Find X
        #     x = nums[i]
        #     y = target - nums[i]
        #     print("X value")
        #     print(x)
        #     print("nums i:", nums[i])
        #     print("target:", target)
        #     # Check First Y 
        #     if (nums.index(y)):
        #         x = nums.index(x)
        #         y = nums.index(y)
        #         return [x, y]
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i







        