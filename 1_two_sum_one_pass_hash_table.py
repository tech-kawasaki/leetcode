class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            completment = target - nums[i]
            if completment in hashmap:
                return [i, hashmap[completment]]
            hashmap[nums[i]] = i