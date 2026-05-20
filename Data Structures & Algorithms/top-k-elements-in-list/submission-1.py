class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1
        # {1: 4, 2: 3, 3: 1}


        arr = []
        for num, freq in count.items():
            arr.append([freq, num])
        arr.sort(reverse=True)
        # [[4, 1], [3, 2], [1, 3]]


        result = []
        for i in range(k):
            result.append(arr[i][1])   
        return result # [1, 2]
        
            