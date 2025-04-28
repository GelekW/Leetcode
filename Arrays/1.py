# Notes:
# Pre-problem thoughts:
# - Unsorted → No 2 pointer (or sort and 2 pointer?)
# - Duplicates allowed
# - Negatives nums and targets allowed
# - Too big too brute-force (n !<= 1000)
# - sort + 2pointer = O(nlogn) + O(n) = O(nlogn), O(1) space
# - hash map = O(n) time, O(n) space 
# - hash map wins
# 
# Problem thoughts:
# - go through arr
# - if compliment of num in dict, return
# - else put in compliment

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for idx, num in enumerate(nums):
            compliment = target - num
            if compliment in compliments:
                return [compliments[compliment], idx]
            else:
                compliments[num] = idx
