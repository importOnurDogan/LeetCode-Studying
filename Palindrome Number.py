"Given an integer X, return TRUE if X is a -palindrome- and FALSE otherwise."
""" 
1: Example
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        c = []
        a = 10
        while True:
            if x > a:
                c.append(x % a)
                a = a * 10
            else:
                break
        c = bool(c)
        return c
