"""This file contains my solution to Leetcode problem 150: Evaluate Reverse Polish Notation."""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []
        operators = set("+-*/")
        for token in tokens:
            if token in operators:
                operandTwo = operandStack.pop()
                operandOne = operandStack.pop()
                result = self.evaluatePostfixExpression(operandOne, operandTwo, token)
                operandStack.append(result)
            else:
                operandStack.append(int(token))    
        return operandStack[-1]
    
    def evaluatePostfixExpression(self, operandOne, operandTwo, operator):
        if operator == "+":
            result = operandOne + operandTwo
        elif operator == "-":
            result = operandOne - operandTwo
        elif operator == "*":
            result = operandOne * operandTwo
        elif operator == "/":
            result = operandOne // operandTwo
            if operandOne * operandTwo < 0 and operandOne % operandTwo != 0:
                result += 1
        return result


# the funny looking if statement for division is to account for expression such as
# -13 // 5 and -5 // 13.
# Another way of writing it is this:
if (operandOne < 0 and operandTwo > 0 or operandTwo < 0 and operandOne > 0) and operandOne % operandTwo != 0:
    results += 1