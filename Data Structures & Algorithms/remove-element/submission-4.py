class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        c = 0
        for i in nums:
            if i == val:
                c += 1
            else:
                nums[k]=nums[c]
                k+=1
                c+=1
        return k