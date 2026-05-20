class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i, n in enumerate(nums):
            nDiff = target - n # nDiff value

            # verify
            if nDiff in dictionary:
                return [dictionary[nDiff], i]

            # adding key/value inside of dictionary but value as key and index as value
            dictionary[n] = i
            # searching for key (n) faster than value (i)
            # {3:0, 4:1, 5:2, 6:3} target 7 - 3 = 4

