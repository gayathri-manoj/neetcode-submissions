class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result=defaultdict(list)
        for i in strs:
             sortedstr = ''.join(sorted(i))
             result[sortedstr].append(i)
        return list(result.values())