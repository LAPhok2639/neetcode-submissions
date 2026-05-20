class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums): #[0:3, 1:4, 2:5, 3:6]
            diff = target - n # diff = 7-4
            if diff in seen: # if 3 not in seen
                return [seen[diff], i] 
            seen[n] = i # add index of 3 in seen {3:0}
                