import os
import random
import shutil
import zipfile
from pathlib import Path

RESOURCES_DIR = './resources/'
OUT_DIR = './out/'
ASSEMBLY_DIR = OUT_DIR + 'assembly/'
INIT_PROGRAM_FILE = RESOURCES_DIR + 'Init_Program.prog_bin'
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
    0x34: [0x00, 0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xB0],
    0x35: [0x00, 0x10, 0x20, 0x30, 0x40, 0x50, 0x60, 0x70, 0x80, 0x90, 0xA0, 0xB0],
    0x37: [0x30, 0x31, 0x32, 0x33],
    0x38: [0x80, 0x84, 0x88, 0x90, 0x94, 0x98, 0xA0, 0xA4, 0xA8, 0xC0, 0xC4, 0xC8, 0xD0, 0xD4, 0xD8, 0xE0, 0xE4, 0xE8],
    0x3B: [0x00, 0x10, 0x20, 0x60, 0x70, 0x80, 0xA0, 0xB0, 0xC0],
    0x3C: [0x3C, 0x3D, 0x3E, 0x7C, 0x7D, 0x7E, 0xBC, 0xBC, 0xBD],
    # TODO: More analysis required for valid voice mode settings.
    # For now, we have the max and min values of each voice mode only.
    0x40: [0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xF8, 0xF9, 0xFA, 0xFB, 0xFC, 0xFD, 0xFE, 0xFF],
    # TODO more analysis required for tempo
    # For now, include only the min, max and default values
    0x64: [0x30, 0x60, 0xB0]
}


def clean():
    shutil.rmtree(OUT_DIR, ignore_errors=True)


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


def write_program(path, program):
    with open(path, 'wb') as f:
        f.write(program)


def assemble():
    with zipfile.ZipFile(os.path.join(OUT_DIR, 'logieminu.mnlgprog'), 'w') as zf:
        zf.write(os.path.join(RESOURCES_DIR, 'FileInformation.xml'), 'FileInformation.xml')
        for file in os.listdir(ASSEMBLY_DIR):
            zf.write(os.path.join(ASSEMBLY_DIR, file), file)
            prog_info_file_name = Path(file).stem + ".prog_info"
            zf.write(os.path.join(RESOURCES_DIR, 'Init_Program.prog_info'), prog_info_file_name)


def pretty_print(program):
    hex_string = ''.join('{:02x}'.format(x) for x in program)
    lines = [hex_string[i:i + LINE_LENGTH] for i in range(0, len(hex_string), LINE_LENGTH)]
    for line in lines:
        print(' '.join(line[i:i+2] for i in range(0, len(line), 2)).upper())


if __name__ == '__main__':
    clean()
    os.makedirs(os.path.dirname(ASSEMBLY_DIR), exist_ok=True)

    program_bytes = read_init_program()
    modify_program(program_bytes)
    write_program(os.path.join(ASSEMBLY_DIR, 'Prog_000.prog_bin'), program_bytes)
    assemble()
