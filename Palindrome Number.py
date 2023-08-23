"Given an integer x, return true if x is a -palindrome- and false otherwise."
""" 
1: Example
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        newx = x
        back_x = 0
        while x > 0:
            back_x = (back_x * 10) + (x % 10)
            x = x // 10
        return newx == back_x



