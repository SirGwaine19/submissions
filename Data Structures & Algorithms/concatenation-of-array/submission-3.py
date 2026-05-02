class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        dou=[]
        for i in range(2):
            for j in nums:
                dou.append(j)
        return dou