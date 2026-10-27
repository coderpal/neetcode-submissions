class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # initialize empty set
        seen = set()

        # loop the nums array
        for num in nums:

            # check if the integer is there in the nums
            if num in seen:
                return True

            # otherwise add that number in the seen set
            seen.add(num)

        return False
        