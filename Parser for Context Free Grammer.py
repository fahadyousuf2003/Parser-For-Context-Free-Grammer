# -*- coding: utf-8 -*-
"""

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bFucvHiuZiofaojJ-OJiy0Ms0vVG9XQJ

"""

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

class Parser:
    def __init__(self, expr):
        self.expr = expr
        self.index = 0

    def parse(self):
        self.index = 0
        result = self.E()
        if self.index != len(self.expr):
            return "Incorrect Structure"
        return result

    def E(self):
        result = self.T()
        while self.index < len(self.expr) and self.expr[self.index] == '+':
            operator = self.expr[self.index]
            self.index += 1
            right = self.T()
            node = Node(operator)
            node.children = [result, right]
            result = node
        return result

    def T(self):
        result = self.F()
        while self.index < len(self.expr) and self.expr[self.index] == '*':
            operator = self.expr[self.index]
            self.index += 1
            right = self.F()
            node = Node(operator)
            node.children = [result, right]
            result = node
        return result

    def F(self):
        if self.index >= len(self.expr):
            return "Incorrect Structure"
        if self.expr[self.index] == '(':
            self.index += 1
            result = self.E()
            if self.index >= len(self.expr) or self.expr[self.index] != ')':
                return "Incorrect Structure"
            self.index += 1
            return result
        if self.expr[self.index] == 'a':
            result = Node('a')
            self.index += 1
            return result
        return "Incorrect Structure"

def print_tree(node, prefix="", is_tail=True):
    if isinstance(node, Node):
        print(prefix + ("└── " if is_tail else "├── ") + node.value)
        for i in range(len(node.children) - 1):
            print_tree(node.children[i], prefix + ("    " if is_tail else "│   "), False)
        if node.children:
            print_tree(node.children[-1], prefix + ("    " if is_tail else "│   "), True)

def test_expression(expr):
    parser = Parser(expr)
    result = parser.parse()
    if result == "Incorrect Structure":
        print(f"Expression: {expr} is incorrect and not part of the given context-free grammar")
    else:
        print(f"Expression: {expr} is correct and part of the given context-free grammer")
        print("It's Parse Tree is given below: ")
        print_tree(result)
    print()

expressions = [
    '(a+a)*a',
    'a*(a*a)+a',
    '(a*a)+(a+a)',
    'a+a)*a',  # Incorrect: Missing opening parenthesis
    '(a+a*a',  # Incorrect: Missing closing parenthesis
    'a+a*a)',  # Incorrect: Missing opening parenthesis
]

for expr in expressions:
    test_expression(expr)
