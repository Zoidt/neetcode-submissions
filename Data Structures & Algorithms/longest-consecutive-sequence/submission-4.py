class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Sort?
        sorted_list = sorted(nums)

        # Create hash set for O(1) look ups
        num_set = set(nums)
        
        # Get starting num
        longest_streak = 0

        # Search for sequence: 
        for n in num_set:

            # If previous does not exist, n may be start of sequence:
            m = n - 1
            if m not in num_set:
                curr_num = n
                curr_streak = 1

                # Find the streak
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                if curr_streak > longest_streak:
                    longest_streak = curr_streak

        
        return longest_streak