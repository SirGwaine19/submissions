class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        not_val=[]
        for i in nums:
            if i != val:
                not_val.append(i)
            continue
        for j in range(len(not_val)):
            nums[j]=not_val[j]
        return len(not_val)