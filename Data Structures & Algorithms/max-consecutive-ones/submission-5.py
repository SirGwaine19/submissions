class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        m = 0
        for i in nums:
            if i == 1:
                c+=1
            else:
                m = max(m,c)
                c=0
        return max(m,c)