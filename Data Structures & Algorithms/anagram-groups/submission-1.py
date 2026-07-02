class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            i1 = "".join(sorted(i))
            if i1 not in res:
                res[i1] = [i]
            else:
                res[i1].append(i)
        return list(res.values())