"""
this is just a try on the jump game problem on leetcode
(which dosn't work because of few small bugs)
but i still find that interesting for a path finder. and i also learned a lot so i will keep that here.
(this solution was also assuming you need to jump the exact number you have in your grid)
"""

class Solution:
    def canJump(self, nums: List[int]) -> bool:
         idx = 0
         saved_pos = []
#need to remove what i don't use.
#add if saved pos only look for left

         while True:
            if idx == (len(nums) - 1) or (idx + nums[idx]) == (len(nums) - 1):
                return True
            if (idx + nums[idx]) < (len(nums)) and nums[idx + nums[idx]] != 0:
                #right then
                saved_pos.append(idx)
                idx = idx + nums[idx]
                pass
            else:
                if (idx - nums[idx]) > 0 and nums[idx - nums[idx]] != 0:
                    #left then
                    idx = idx - nums[idx]
                    nums[idx] = 0
                    pass
                else:
                    if saved_pos:
                        #saved pos then
                        pass
                        idx = saved_pos[-1]
                        saved_pos.pop()
                    else:
                        return False
