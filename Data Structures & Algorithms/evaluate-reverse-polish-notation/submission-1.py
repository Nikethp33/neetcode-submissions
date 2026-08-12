import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_mapping = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        for i in range(len(tokens)):
            if tokens[i] not in ["+",'-','*','/']:
                stack.append(tokens[i])
            else:
                ele2 = stack.pop()
                ele1 = stack.pop()
                val = int(operator_mapping[tokens[i]](int(ele1),int(ele2)))
                stack.append(val)
        res = int(stack.pop())
        return res
        