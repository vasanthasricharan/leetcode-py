class Solution:
    def isValid(self, s):
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return s == ''

sol = Solution()


user_input = input("Enter a string of parentheses: ")


if sol.isValid(user_input):
    print("✅ Valid parentheses.")
else:
    print("❌ Invalid parentheses.")
