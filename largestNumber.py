class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(i) for i in nums]
        
        def custom_sort(a,b):
            if a + b > b + a:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(custom_sort))
        
        while nums[0] == '0' and len(nums) > 1:
            nums.pop(0)
        
        return "".join(nums)
