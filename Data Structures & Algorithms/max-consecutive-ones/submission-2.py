class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        con = [0]
        for i in nums:
            if i == 1:
                c+= 1
            else:
                con.append(c)
                c=0
        con.append(c)
        return max(con)