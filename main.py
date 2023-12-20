import os
import random

INIT_PROGRAM_FILE = './resources/Init_Program.prog_bin'
BIN_OUT_FILE = './out/Prog_000.prog_bin'
PROGRAM_NAME = 'Logieminu 1'
LINE_LENGTH = 32

ANY_BYTE = list(range(0, 0xFF))
FIDDLEABLE_BYTES = {
    0x14: ANY_BYTE,
    0x15: ANY_BYTE,
    0x16: ANY_BYTE,
    0x17: ANY_BYTE,
    0x18: ANY_BYTE,
    0x19: ANY_BYTE,
    0x1A: ANY_BYTE,
    0x1B: ANY_BYTE,
    0x1C: ANY_BYTE,
    0x1D: ANY_BYTE,
    0x1E: ANY_BYTE,
    0x1F: ANY_BYTE,
    0x22: ANY_BYTE,
    0x23: ANY_BYTE,
    0x24: ANY_BYTE,
    0x25: ANY_BYTE,
    0x26: ANY_BYTE,
    0x27: ANY_BYTE,
    0x28: ANY_BYTE,
    0x29: ANY_BYTE,
    0x2A: ANY_BYTE,
    0x2B: ANY_BYTE,
    0x31: ANY_BYTE,
    0x32: ANY_BYTE,
    0x33: ANY_BYTE,
}


def read_init_program():
    with open(INIT_PROGRAM_FILE, 'rb') as f:
        return bytearray(f.read())


def modify_program(program):
    # Set the program name at position 0x00000004, fixed length 16
    program_name_bytes = '{:16.16}'.format(PROGRAM_NAME).encode('utf-8')
    program[4:len(program_name_bytes) + 4] = program_name_bytes

    # Randomize all known program parameters
    for offset, allowed_values in FIDDLEABLE_BYTES.items():
        program[offset] = random.choice(allowed_values)


def write_program(program):
    print(f'Writing bytes to {BIN_OUT_FILE}')
    pretty_print(program)

    os.makedirs(os.path.dirname(BIN_OUT_FILE), exist_ok=True)
    with open(BIN_OUT_FILE, 'wb') as f:
        f.write(program)


def pretty_print(program):
    hex_string = ''.join('{:02x}'.format(x) for x in program)
    lines = [hex_string[i:i + LINE_LENGTH] for i in range(0, len(hex_string), LINE_LENGTH)]
    for line in lines:
        print(' '.join(line[i:i+2] for i in range(0, len(line), 2)).upper())


if __name__ == '__main__':
    program_bytes = read_init_program()
    modify_program(program_bytes)
    write_program(program_bytes)
