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
                stack.append(int(tokens[i]))
            else:
                ele2 = stack.pop()
                ele1 = stack.pop()
                if tokens[i] == "/":
                    val = int(ele1/ele2)
                else:
                    val = operator_mapping[tokens[i]](ele1,ele2)
                stack.append(val)
        res = stack.pop()
        return res
        