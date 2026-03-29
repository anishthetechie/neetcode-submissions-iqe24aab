class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1): # 4-1 == 3 => [0, 1, 2]
            if nums[i] == nums[i+1]:
                return True
        return False
