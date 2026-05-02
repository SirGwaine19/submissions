class Solution:
    def reverseString(self, s: List[str]) -> None:
        l,r=0,len(s)-1
        res=[]
        while l<r:
            s[l],s[r]=s[r],s[l]
            res.append(s[l])
            l,r=l+1,r-1
        