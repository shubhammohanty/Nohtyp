import argparse

parser = argparse.ArgumentParser(description="""
An esoteric language which is just the reverse of python ~~ usage: nohtyp [option] [-h help | -I Interactive | -V version |] [arg] ...
""")


def lexer(commands):
    for command in commands:
        command = command[::-1]
        exec(command)

def codeParser(fname):
    if fname[-3:] == '.yp':
        with open(fname, 'r') as f:
           commands = tuple(f.readlines())
           lexer(commands=commands)
    else:
        print("Invalid File extension!!, not a nohtyp file!!")


parser.add_argument(
    'fileName',
    type = str,
    help = "Enter the .yp filename as an argument to run your nohtyp file"
)


__version_info__ = ('0.0.1')
__version__ = (__version_info__)
...
parser.add_argument('-V', '--version', action='version', version="%(prog)s ("+__version__+")")

args = parser.parse_args()


fname = args.fileName


if args.fileName:
    codeParser(fname=fname)



