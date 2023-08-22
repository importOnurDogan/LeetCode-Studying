"Given an integer x, return true if x is a -palindrome- and false otherwise."
""" 
1: Example
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or x == 10:
            return False
        if 0 <= x < 10:
            return True
        a = 10
        new_x = []
        while (x / a) > a:
            new_x.append(x % a)
            new_x.append((x / a) % a)
            a = a * 10
            new_x.append(x / a)
        new_x = bool(new_x)
        if x == new_x:
            return True


