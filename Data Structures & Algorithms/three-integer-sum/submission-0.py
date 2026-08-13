class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,n in enumerate(nums):
            # This ends the loop if there are no possible 0 combos
            if n > 0:
                break
            # This handles the dupes
            if i > 0 and n == nums[i-1]:
                continue

            # Set left pointer to be i+1 since i is our iterator
            # Set pointer is the end pointer decrementing
            l,r = i+1, len(nums)-1
            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    res.append([n, nums[l], nums[r]])
                    l+=1
                    # Incrementing r because 0 is found so any value after using nums[r] will be > 0
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res

        # Why sort? Sorting is its own operation and is irrelevant to the existing O(n^2) leading time complexity