class Solution:
    def trap(self, height: List[int]) -> int:
        # variables
        size = len(height)
        max_left = []
        max_right = [0] * size
        curr_max = 0

        # find max on left
        for n in height:
            curr_max = max(curr_max, n)
            max_left.append(curr_max)

        print(max_left)

        # find max on right
        curr_max = 0
        for i in range(len(height)- 1, -1, -1):
            curr_max = max(curr_max, height[i])
            max_right[i] = curr_max
        print(max_right)

        trapped_water = 0
        for i in range(len(height) - 1):
            lowest = min(max_left[i], max_right[i])
            trapped_water += lowest - height[i]

        return trapped_water