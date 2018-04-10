import argparse
from src import target
from src import verify
from src import solve
from src import actions

def main():
    parser = getParser()
    args = parser.parse_args()

    if (args.cmd == target.COMMAND):
        target.run(args, parser)
    elif (args.cmd == solve.COMMAND):
        solve.run(args, parser)
    elif (args.cmd == verify.COMMAND):
        verify.run(args, parser)
    else:
        parser.print_help()

def getParser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", help="Shows this help message or command help and exit", nargs="?", const="", default="", action=actions.HelpAction, metavar="CMD")
    subparsers = parser.add_subparsers(help="Commands", dest="cmd")
    target.setup(subparsers)
    solution.setup(subparsers)
    verify.setup(subparsers)
    return parser

if __name__ == "__main__":
    main()

