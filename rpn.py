#!/usr/bin/env python3

def calculate(string):
    stack = list()
    for token in string.split():
        if token == '+':
            arg1 = stack.pop()
            arg2 = stack.pop()
            result = arg1 + arg1
            stack.append(result)
        elif token == '-':
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = arg1 - arg2
            stack.append(result)
        else:
            stack.append(int(token))
    if len(stack) != 1:
        raise TypeError('Malformed input: ' + string)
    return stack.pop()

def main():
    while True:
        calculate(input('rpm calc> '))


if __name__ == '__main__':
    main()

