import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b: int(a / b)
        }
        for char in tokens:
            if char.lstrip('-').isdigit():
                stack.append(int(char))
            elif char in operators:
                pop_1 = stack.pop()
                pop_2 = stack.pop()
                calc_function = operators[char]
                stack.append(calc_function(pop_2, pop_1))
        return stack[-1]
                
