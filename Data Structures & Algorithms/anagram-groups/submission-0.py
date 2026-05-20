class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for word in strs:
            same = tuple(sorted(word))

            if same not in grouped:
                grouped[same] = []
            grouped[same].append(word)
        
        return list(grouped.values())