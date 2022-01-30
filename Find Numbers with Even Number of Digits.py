...
[22-01-30]  Max Consecutive Ones
https://leetcode.com/explore/learn/card/fun-with-arrays/521/introduction/3237/
...
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            count = 0
            while num > 0:
                num = num // 10
                count = count + 1
            if count % 2 == 0:
                total = total + 1
        return total;
      
      
      
      
      =============================================== solution2
      
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # // 0-9 > 0
        # // 10-99> e
        # // 100- 999> o
        # // 1000-9999> e
        # // 10000 -99999 > o
        # // 100000 > e
        
        total = 0
        for num in nums:
            if (num >= 100000 and num <= 999999) or (num>=1000 and num<=9999) or (num>=10 and num<=99):
                total = total + 1
        return total;
