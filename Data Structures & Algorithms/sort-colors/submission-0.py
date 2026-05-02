class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        cont= [0]*3
        for i in nums:
            cont[i]+=1
        p=0
        for j in range(len(cont)):
            for k in range(cont[j]):
                nums[p]=j
                p+=1
        return nums


        
        