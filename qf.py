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

    @staticmethod
    def from_bf(bf_code):
        """Import Brainfuck code"""
        code = [Qf.INST[Qf.BF_INST.index(c)] for c in bf_code if c in Qf.BF_INST]
        return Qf(code)

    def __str__(self):
        """Print code"""
        return "".join(self.code)

    def run(self, data):
        """Execute the code on a data array"""
        i = 0
        pc = 0
        lr = []
        while pc < len(self.code):
            op = self.code[pc]
            if op == self.INST[0]:
                i -= 1
                pc += 1
            elif op == self.INST[1]:
                i += 1
                pc += 1
            elif op == self.INST[2]:
                data[i] -= 1
                pc += 1
            elif op == self.INST[3]:
                data[i] += 1
                pc += 1
            elif op == self.INST[4]:
                print(chr(data[i]), end="")
                pc += 1
            elif op == self.INST[5]:
                try:
                    # Use getch package to read single character from user
                    import getch
                    data[i] = ord(getch.getch())
                    pc += 1
                except:
                    print("Need getch package to do character input.")
                    print("Install using pip:")
                    print("  pip install getch")
                    exit(1)
            elif op == self.INST[6]:
                if data[i] != 0:
                    lr.append(pc)
                    pc += 1
                else:
                    # Jump to end of loop
                    depth = 1
                    while depth > 0:
                        pc += 1
                        if self.code[pc] == self.INST[6]:
                            depth += 1
                        if self.code[pc] == self.INST[7]:
                            depth -= 1
                    pc += 1
            elif op == self.INST[7]:
                pc = lr.pop()

        return data

def main():
    parser = argparse.ArgumentParser(description="A Quotefuck interpreter")
    parser.add_argument("filename")
    parser.add_argument("--bf", action="store_true", help="Import Brainfuck code")
    parser.add_argument("-p", "--print_code", action="store_true", help="Print code and exit")
    parser.add_argument("-o", "--print_output", action="store_true", help="Print the memory after execution")
    parser.add_argument("-m", "--memory_size", type=int, default=256, help="Memory size")
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
        # Execute code
        output = qf.run(input)

        if args.print_output:
            print(output)


if __name__ == "__main__":
    main()
