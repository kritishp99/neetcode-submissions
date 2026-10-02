class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c={}
        for n in nums:
            if n in c:
                c[n]+=1
            else:
                c[n]=1
        un=list(c.keys())
        un.sort(key=lambda x:c[x],reverse=True)
        return un[:k]
                        
        