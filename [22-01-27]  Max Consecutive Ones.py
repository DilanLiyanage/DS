...
[22-01-27]  Max Consecutive Ones
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3238/
...

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count = 0
        maxcount = 0
        
        for n in nums:
            if n == 1: count = count + 1
            else:
                if count>maxcount: maxcount = count
                count = 0
        if count>maxcount: maxcount = count
        
        return maxcount;
                
