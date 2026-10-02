class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res={}
        for st in strs:
            s="".join(sorted(st))
            if s not in res:
                res[s]=[]
            res[s].append(st)
        return list(res.values())