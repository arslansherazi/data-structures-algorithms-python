from data_structures.stack.stack import Queue


class PostfixExpressionEvaluator(object):
    """
    45+7*2-   =======>   61
    """
    def __init__(self):
        self.stack = Queue()
        self.operators = ['+', '-', '*', '/', '^']

    def evaluate_postfix_expression(self, expression):
        for exp in expression:
            if exp not in self.operators:
                self.stack.push(exp)
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                result = str(eval(operand2 + exp + operand1))
                self.stack.push(result)
        print(f'\nResult of Postfix Expression Evaluation:: {self.stack.pop()}')


if __name__ == '__main__':
    postfix_expression = input('Enter postfix expression:: ')
    postfix_expression_evaluation = PostfixExpressionEvaluator()
    postfix_expression_evaluation.evaluate_postfix_expression(postfix_expression)

