# class Solution:
#     def evalRPN(tokens):
#         ans = []
#         for i in tokens:
#             if i not in ["+", "-", "/", "*"]:
#                 ans.append(int(i))
#             else:
#                 a = ans.pop()
#                 b = ans.pop()
#                 if i == "+":
#                     ans.append(a + b)
#                 elif i == "-":
#                     ans.append(b - a)
#                 elif i == "*":
#                     ans.append(a * b)
#                 elif i == "/":
#                     ans.append(int(b / a))
#         return ans[-1]

# obj = Solution
# tokens = ["2", "1", "+", "3", "*"]
# r = obj.evalRPN(tokens)
# print(r)