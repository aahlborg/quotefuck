#!/usr/bin/env python3

import argparse


class Qf:
    # Instruction set
    INST = ["“", "”", "‘", "’", '"', "'", "`", "´"]
    # Brainfuck instruction set
    BF_INST = ["<", ">", "-", "+", '.', ",", "[", "]"]

    def __init__(self, code):
        """Create a program from a string containing the code"""
        self.code = [c for c in code if c in self.INST]
        self.r0 = 0
        self.pc = 0
        self.lr = []
        self.memory = [0] * 256

    @staticmethod
    def from_bf(bf_code):
        """Import Brainfuck code"""
        code = [Qf.INST[Qf.BF_INST.index(c)] for c in bf_code if c in Qf.BF_INST]
        return Qf(code)

    def __str__(self):
        """Print code"""
        return "".join(self.code)

    def debug_print(self):
        print(f"r0: {self.r0} ({self.memory[self.r0]})")
        print(f"pc: {self.pc} ({self.code[self.pc]})")
        print(f"lr: {self.lr}")

    def step(self):
        """Execute a single instruction"""
        op = self.code[self.pc]

        if op == self.INST[0]:
            self.r0 -= 1
            self.pc += 1
        elif op == self.INST[1]:
            self.r0 += 1
            self.pc += 1
        elif op == self.INST[2]:
            self.memory[self.r0] -= 1
            self.pc += 1
        elif op == self.INST[3]:
            self.memory[self.r0] += 1
            self.pc += 1
        elif op == self.INST[4]:
            print(chr(self.memory[self.r0]), end="")
            self.pc += 1
        elif op == self.INST[5]:
            try:
                # Use package getch to read single character from user
                import getch
                self.memory[self.r0] = ord(getch.getch())
                self.pc += 1
            except:
                print("Need package getch to read a character.")
                print("Install using pip:")
                print("  pip install getch")
                exit(1)
        elif op == self.INST[6]:
            if self.memory[self.r0] != 0:
                self.lr.append(self.pc)
                self.pc += 1
            else:
                # Jump to end of loop
                depth = 1
                while depth > 0:
                    self.pc += 1
                    if self.code[self.pc] == self.INST[6]:
                        depth += 1
                    if self.code[self.pc] == self.INST[7]:
                        depth -= 1
                self.pc += 1
        elif op == self.INST[7]:
            self.pc = self.lr.pop()

    def run(self, data):
        """Execute the code on a data array"""
        self.memory = data

        while self.pc < len(self.code):
            self.step()

        return self.memory

def main():
    parser = argparse.ArgumentParser(description="A Quotefuck interpreter")
    parser.add_argument("filename")
    parser.add_argument("--bf", action="store_true", help="Import Brainfuck code")
    parser.add_argument("-p", "--print_code", action="store_true", help="Print code and exit")
    parser.add_argument("-o", "--print_output", action="store_true", help="Print the memory after execution")
    parser.add_argument("-m", "--memory_size", type=int, default=256, help="Memory size")
    parser.add_argument("-i", "--input_data", help="Input data, spearated by comma")
    args = parser.parse_args()

    with open(args.filename, "r") as f:
        code = f.read()

        if args.bf:
            qf = Qf.from_bf(code)
        else:
            qf = Qf(code)

        if args.print_code:
            print(qf)
            return

        # Create input array
        input = [0] * args.memory_size
        if args.input_data:
            data = args.input_data.split(",")
            for i in range(len(data)):
                input[i] = int(data[i])

        # Execute code
        output = qf.run(input)

        if args.print_output:
            print(output)


if __name__ == "__main__":
    main()
