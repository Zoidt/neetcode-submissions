class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # prefix
        prefix = 1
        for i in range(len(nums)):
            print("Prefix - Step:", i + 1)
            res[i] = prefix 
            prefix *= nums[i]
            print(nums)
            print(res)

        print("============ POSTFIX ================")
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            print("Postfix - Step:", i + 1)
            print("Math: Res[i] *= postfix:", res[i], "*=", postfix)
            res[i] *= postfix 
            print("Math: postfix *= nums[i]:", postfix, "*=", nums[i])
            postfix *= nums[i]
            print(nums)
            print(res)

        return res