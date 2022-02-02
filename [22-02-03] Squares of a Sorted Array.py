'''
[22-02-03] Squares of a Sorted Array.py
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3240/

'''

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        count = len(nums) - 1
        #[-4,-1,0,3,10]
        #[16,1, 0,9,100]
        #R[0,0,0,0,0]
        #[0,1,9,16,100]
        
        while(l <= r):
            ls = nums[l] * nums[l]
            rs = nums [r] * nums [r]
            if ( ls > rs):
                result[count] = ls
                count = count - 1
                l = l + 1                
            else:
                result[count] = rs
                count = count - 1
                r = r - 1
                
        return result
                
