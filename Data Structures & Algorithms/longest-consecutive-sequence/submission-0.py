class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        l=0
        for n in s:
            if (n-1) not in s:
                leng=1
                while (n+leng) in s:
                    leng+=1
                l=max(l,leng)
        return l

        