class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        actual_num = []
        for num in range(len(nums)):
            if nums[num] != val:
                actual_num.append(nums[num])
        for i in range(len(actual_num)):
            nums[i] = actual_num[i]
        return len(actual_num)

        
        