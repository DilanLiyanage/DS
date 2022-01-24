'''
[22-01-24] Squares of a Sorted Array
https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3240/
'''
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        count = len(nums) - 1
        #[-4,-1,0,3,10]
        
        while(l <= r):
            ls = nums[l] * nums[l]
            rs = nums [r] * nums [r]
            if ( ls > rs):
                result[count] = ls
                
