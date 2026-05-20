class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # initialize the empty dictionary
        seen = {}

        # for loop left to right, using enumerate
        for index, num in enumerate(nums):

            # core logic
            complement = target - num

            # if the complement exists in the seen
            if complement in seen:

                # return the complements index and the current position index
                return [seen[complement], index]

            # if complement is not found, store the num and its index in seen
            # can be used further in the loop if core logic fulfilled
            seen[num] = index
        