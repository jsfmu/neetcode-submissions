class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        c = {')': '(', '}': '{', ']': '['}

        # Traverse string
        for i in s:
            if i in c:
                # If the stack isn't empty and the values align by the dictionary
                if stack and stack[-1] == c[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return not stack