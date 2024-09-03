class StackCalc:
    def __init__(self):
        self.stack = []

    def run(self, instructions):
        for el in instructions.split():
            if el.isnumeric():
                self.stack += [int(el)]
            elif el == '+':
                self.stack = self.stack[:-2] + [sum(self.stack[-2:])]
            elif el == '-':
                self.stack = self.stack[:-2] + [self.stack[-1] - self.stack[-2]]
            elif el == '*':
                self.stack = self.stack[:-2] + [self.stack[-1] * self.stack[-2]]
            elif el == '/':
                self.stack = self.stack[:-2] + [self.stack[-1] / self.stack[-2]]
            elif el == 'DUP':
                self.stack += [self.stack[-1]]
                print(self.stack)
            elif el == 'POP':
                print(self.stack.pop())
            elif el == 'PSH':
                pass
            else:
                self.stack = [f'Недействительная инструкция: {el}']
                break


    def getValue(self):
        return 0 if len(self.stack) == 0 else self.stack[-1]

if __name__ == '__main__':
    calc = StackCalc()
    calc.run('2 5 +')
    print(calc.getValue())

    calc.run('2 5 -')
    print(calc.getValue())

    calc.run('2 5 *')
    print(calc.getValue())

    calc.run('2 5 /')
    print(calc.getValue())

    calc.run('2 5 DUP')
    print(calc.getValue())

    calc.run('2 5 POP')
    print(calc.getValue())

    calc.run('2 5 a')
    print(calc.getValue())








