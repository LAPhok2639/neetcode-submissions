class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for n in strs:
            key = "".join(sorted(n))
            if key not in grouped:
                grouped[key] = []
            grouped[key].append(n)
        # {"act": ["act", "cat"]}
                
        result = []
        for val in grouped.values():
            result.append(val)
        
        return result
        # [["act", "cat"], ["stop", "pots", "tops"]]
