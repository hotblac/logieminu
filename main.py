INIT_PROGRAM_FILE = './resources/Init_Program.prog_bin'
PROGRAM_NAME = "Logiemin 1"
LINE_LENGTH = 32


def read_init_program():
    with open(INIT_PROGRAM_FILE, 'rb') as f:
        return bytearray(f.read())


def modify_program(program):
    # Set the program name at position 0x00000004, fixed length 16
    program_name_bytes = '{:16.16}'.format(PROGRAM_NAME).encode('utf-8')
    program[4:len(program_name_bytes)] = program_name_bytes


def write_program():
    pass


def pretty_print(program):
    hex_string = ''.join('{:02x}'.format(x) for x in program)
    lines = [hex_string[i:i + LINE_LENGTH] for i in range(0, len(hex_string), LINE_LENGTH)]
    for line in lines:
        print(' '.join(line[i:i+2] for i in range(0, len(line), 2)).upper())


if __name__ == '__main__':
    program_bytes = read_init_program()
    modify_program(program_bytes)
    pretty_print(program_bytes)
