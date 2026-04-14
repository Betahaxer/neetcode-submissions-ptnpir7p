class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for token in tokens:
            if token in {'+', '-', '*', '/'}:
                operand_2 = operands.pop()
                operand_1 = operands.pop()
                if token == "+":
                    operands.append(operand_1 + operand_2)
                elif token == "-":
                    operands.append(operand_1 - operand_2)
                elif token == "*":
                    operands.append(operand_1 * operand_2)
                else:
                    operands.append(int(operand_1 / operand_2))
            else:
                operands.append(int(token))
        return operands[0]