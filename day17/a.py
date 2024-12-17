import sys


ADV = 0
BXL = 1
BST = 2
JNZ = 3
BXC = 4
OUT = 5
BDV = 6
CDV = 7


def get_input():
    lines = sys.stdin.readlines()
    input_str = ''.join(lines)
    return input_str


def get_registers(input_str):
    registers_str, _ = input_str.split('\n\n')
    registers_str = registers_str.strip()

    register_lines = registers_str.split('\n')

    register_values = []
    for line in register_lines:
        _, register_value = line.split(':')
        register_values.append(int(register_value))
    return register_values


def get_program(input_str):
    _, program_line = input_str.split('\n\n')
    program_line = program_line.strip()

    _, program_str = program_line.split(':')

    program = [int(value) for value in program_str.split(',')]

    return program


def get_combo(operand, registers):
    A, B, C = registers

    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        raise Exception


def get_literal(operand):
    return operand


def execute(instruction_pointer, program, registers, screen):
    A, B, C = registers

    instruction = program[instruction_pointer]
    operand = program[instruction_pointer+1]

    if instruction == ADV:
        combo_operand = get_combo(operand, registers)
        result = A // 2**combo_operand
        A = result
    elif instruction == BXL:
        literal_operand = get_literal(operand)
        result = B ^ literal_operand
        B = result
    elif instruction == BST:
        combo_operand = get_combo(operand, registers)
        result = combo_operand % 8
        B = result
    elif instruction == JNZ:
        if A == 0:
            registers = A, B, C
            return instruction_pointer+2, registers, screen
        literal_operand = get_literal(operand)
        instruction_pointer = literal_operand

        registers = A, B, C
        return instruction_pointer, registers, screen
    elif instruction == BXC:
        result = B ^ C
        B = result
    elif instruction == OUT:
        combo_operand = get_combo(operand, registers)
        result = combo_operand % 8
        screen.append(result)
    elif instruction == BDV:
        combo_operand = get_combo(operand, registers)
        result = A // 2**combo_operand
        B = result
    elif instruction == CDV:
        combo_operand = get_combo(operand, registers)
        result = A // 2**combo_operand
        C = result

    registers = A, B, C

    return instruction_pointer+2, registers, screen


def main(registers, program):
    screen = []
    instruction_pointer = 0
    while True:
        if instruction_pointer >= len(program):
            break

        instruction_pointer, registers, screen = execute(
            instruction_pointer,
            program,
            registers,
            screen
        )

    return registers, screen


def test1():
    input_str = """Register A: 729
Register B: 0
Register C: 9

Program: 2,6"""
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    A, B, C = registers

    if B == 1:
        print('✅')
    else:
        print('❌')


def test2():
    input_str = """Register A: 10
Register B: 0
Register C: 9

Program: 5,0,5,1,5,4"""
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    A, B, C = registers

    if screen == [0, 1, 2]:
        print('✅')
    else:
        print('❌')


def test3():
    input_str = """Register A: 2024
Register B: 0
Register C: 9

Program: 0,1,5,4,3,0"""
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    A, B, C = registers

    try:
        assert screen == [4,2,5,6,7,7,7,7,3,1,0]
        assert A == 0
        print('✅')
    except:
        print('❌')


def test4():
    input_str = """Register A: 2024
Register B: 29
Register C: 9

Program: 1,7"""
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    A, B, C = registers

    try:
        assert B == 26
        print('✅')
    except:
        print('❌')


def test5():
    input_str = """Register A: 2024
Register B: 2024
Register C: 43690

Program: 4,0"""
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    A, B, C = registers

    try:
        assert B == 44354
        print('✅')
    except:
        print('❌')


if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()

    input_str = get_input()
    registers = get_registers(input_str)
    program = get_program(input_str)

    registers, screen = main(registers, program)

    print(','.join(map(str, screen)))

