class Solution:
    def sortColors(self, nums: List[int]) -> None:
        col=[0]*3
        for i in nums:
            col[i]+=1
        i = 0
        for n in range(len(col)):
            for j in range(col[n]):
                nums[i]=n
                i+=1
        return nums
