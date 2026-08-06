class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while left < right and not s[left].isalnum(): # While left < right and s[left] is NOT a number/char, skip. This means we gonna keep incrementing if not a char/num
                left += 1
            while right > left and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    # Function to check if the string at the an index is a num/char
    # def isalnumb(self, c):
    #     return (ord('A') <= ord(c) <= ord('Z') or 
    #     ord('a') <= ord(c) <= ord('z') or 
    #     ord('0') <= ord(c) <= ord('9'))