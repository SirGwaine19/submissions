class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m=[]
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count+=1
            else:
                m.append(count)
                count=0
            m.append(count)
        return max(m)
