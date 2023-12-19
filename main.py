INIT_PROGRAM_FILE = './resources/Init_Program.prog_bin'
LINE_LENGTH = 32


def read_init_program():
    with open(INIT_PROGRAM_FILE, 'rb') as f:
        return bytearray(f.read())


def write_program():
    pass


def pretty_print(program):
    hex_string = ''.join('{:02x}'.format(x) for x in program)
    lines = [hex_string[i:i + LINE_LENGTH] for i in range(0, len(hex_string), LINE_LENGTH)]
    for line in lines:
        print(' '.join(line[i:i+2] for i in range(0, len(line), 2)).upper())


if __name__ == '__main__':
    program = read_init_program()
    pretty_print(program)
