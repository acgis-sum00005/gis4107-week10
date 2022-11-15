import os
import sys
from fix_haiti_file import fix_file

def main():
    """The main flow to fix_haiti_file"""
    if len(sys.argv) != 3:
        print("Usage: fix_haiti_file_cli.py input_file fixed_file")
        sys.exit()
    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist!\nAre you sure you spelled it correctly?")
    fix_file(in_csv=input_file, out_csv=sys.argv[2])

if __name__ == '__main__':
    main()