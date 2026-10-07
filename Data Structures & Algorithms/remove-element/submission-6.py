class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i]==val:
                nums[i]=nums[j]
                j-=1
            continue
        return j+1