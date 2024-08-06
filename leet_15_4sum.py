class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        final = []
        n = len(nums)
        
        for j in range(n - 3):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            for i in range(j + 1, n - 2):
                if i > j + 1 and nums[i] == nums[i - 1]:
                    continue
                left, right = i + 1, n - 1
                while left < right:
                    total = nums[j] + nums[i] + nums[left] + nums[right]
                    if total == target:
                        final.append([nums[j], nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total > target:
                        right -= 1
                    else:
                        left += 1
        return final
