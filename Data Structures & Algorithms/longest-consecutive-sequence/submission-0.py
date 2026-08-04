class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # What we're working with: 
        # 1) A list nums
        # 2) A streak counter
        # 3) 

        # Limitations:
        # 1) The streak counter has to be a single variable that changes as we iterate (we can use max())
        # 2) If we have a number that is -1 lower than the value, this is not the start of the sequence, so skip

        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num-1) not in numSet: # Condition because his wouldn't be the start of the sequence, reducing overhead
                length = 1
                while (num+length) in numSet: # using the num+length which is consistently updates
                    length += 1
                longest = max(length, longest)
        return longest