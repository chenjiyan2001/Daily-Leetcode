class Solution:
#     # 1. O(n^2) t:2828ms(34%) m:15.2M(73%)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for idx1 in range(len(nums)-1):
#             for idx2 in range(idx1+1, len(nums)):
#                 if nums[idx1] + nums[idx2] == target:
#                     return [idx1, idx2]
    
#     # 2. O(nlogn) t:40ms(61%) m:16.1M(?%)
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums = list(enumerate(nums))
#         nums.sort(key=lambda x:x[1])
#         begin, end = 0, len(nums)-1
#         while begin < end:
#             sum = nums[begin][1] + nums[end][1]
#             if sum == target:
#                 return [nums[begin][0], nums[end][0]]
#             elif sum > target:
#                 end -= 1
#             else:
#                 begin += 1
    
#     # 3. O(n) t:40ms(61%) m:15.9M(15%) Hash1
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#             map = {v:k for k,v in enumerate(nums)} # 实际上有问题, 键相同时值会覆盖, 但条件"两数"恰好使得结果正确
#             for i, num in enumerate(nums):
#                 j = map.get(target - num)
#                 if j is not None and j != i:
#                     return [i, j]
    
    # 4. O(n) t:36ms(75%) m:15.8M(20%) Hash2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
          map = {}
          for i, num in enumerate(nums):
              j = map.get(target - num)
              if j is not None:
                  return [j, i]
              map[num] = i
