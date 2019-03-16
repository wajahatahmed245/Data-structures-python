import numpy as np


class Stack:
    def __init__(self, expression_for_evaluation=" "):
        self.stack_list = []
        self.expression_for_evaluation = expression_for_evaluation

    def push(self, element_for_stack=None):
        if self.expression_for_evaluation != " ":
            for i in range(0, len(self.expression_for_evaluation)):
                self.stack_list.append(self.expression_for_evaluation[i])
        else:
            self.stack_list.append(element_for_stack)

    def display_stack(self):
        stack = np.array(self.stack_list)
        # print(stack)
        return stack

    def pop(self):
        if not self.stack_list:
            print("stack underflow")
        else:
            top = len(self.stack_list) - 1
            removed_elements = self.stack_list[top]
            print("The element {} is removed".format(removed_elements))
            self.stack_list.pop()

    def reverse_stack(self):
        reversed_arr = self.display_stack()[::-1]
        print("The reverse of stack is {}".format(reversed_arr))

    def top_stack(self):

        if len(self.stack_list) == 0:
            return -1

        elif len(self.stack_list) == 1:
            return "!@!", self.stack_list[0]

        else:
            length = len(self.stack_list)
            top = length - 1
            top_value = self.stack_list[top]
            return top_value
        return None


def priorties(argument):
    switcher = {
        "(": 1.2,
        ")": 1,
        "^": 2,
        "*": 3,
        "/": 3,
        "+": 4,
        "-": 4,
    }
    return switcher.get(argument, "0")


def infix_Postfix(expression):
    stack = Stack()
    operations = []
    output = ""

    for i in range(0, len(expression)):
        operations.append(priorties(expression[i]))

    for index in range(0, len(expression)):
        if operations[index] == "0":
            output = output + expression[index]

        elif operations[index] != "0":

            if stack.top_stack() == -1:
                stack.push(expression[index])

            elif int(priorties(stack.top_stack())) > int(operations[index]):
                stack.push(expression[index])

            elif stack.top_stack() == "(":
                stack.push(expression[index])

            elif stack.top_stack() == ")":
                while True:

                    if stack.top_stack() != "(" or stack.top_stack() != ")":
                        output = output + stack.top_stack()

                    stack.pop()

                    if stack.top_stack() == "(":
                        break

            elif stack.top_stack()[0] == "!@!":
                output = output + stack.top_stack()[1]

    return operations, output


expressions = input("write your Expression : ")
print(infix_Postfix(expressions))
# print("lenth of string is {}".format(len(expression)))


# stack.push(1)
# stack.push(3)
# stack.push(4)
# print(stack.top_stack())
# #
# # stack.push()
