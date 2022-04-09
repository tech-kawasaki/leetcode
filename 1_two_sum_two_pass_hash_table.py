class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            completement = target - nums[i]
            if completement in hashmap and hashmap[completement] != i:
                return [i, hashmap[completement]]