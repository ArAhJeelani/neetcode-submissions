class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for index, num in enumerate(nums):
            hashmap[num] = index #this print 2: 0 4: 1 5: 2
        for i in range(len(nums)):
            if (target-nums[i]) in hashmap and (i != hashmap[target-nums[i]]):
                return [i, hashmap[target-nums[i]]]

 

