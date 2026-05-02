class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        c = 0
        for i in nums:
            if i != val:
                nums[k]=nums[c]
                k+=1
                c+=1
            else:
                c+=1
        return k