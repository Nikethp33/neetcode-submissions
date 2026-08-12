import operator 

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_mapping = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
        }

        for i in range(len(tokens)):
            if tokens[i] not in ["+",'-','*','/']:
                stack.append(tokens[i])
            else:
                ele2 = int(stack.pop())
                ele1 = int(stack.pop())
                if tokens[i] == "/":
                    val = int(ele1/ele2)
                else:
                    val = operator_mapping[tokens[i]](ele1,ele2)
                stack.append(val)
        res = int(stack.pop())
        return res
        