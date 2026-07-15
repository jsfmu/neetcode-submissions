class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.add(i)
        # return False

        # return Counter(nums) != Counter(set(nums))