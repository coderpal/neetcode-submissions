class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # initialize dictionary that will store numbers and its indices
        seen = {}

        # loop through the array with enumerate (also gives index)

        for i, num in enumerate(nums):

            # validate the formula
            diff = target - num

            # check if the num is already in seen dictionary
            if diff in seen:
                return [seen[diff], i]

            # if not in seen, add that number
            seen[num] = i

