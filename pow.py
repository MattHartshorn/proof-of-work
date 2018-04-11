import argparse
from src import target
from src import verify
from src import solve
from src import parserhelper

def main():
    # Setup the parser
    parser, subparsers = parserhelper.getParser()
    target.setup(subparsers)
    solve.setup(subparsers)
    verify.setup(subparsers)

    # Parse the args and run the desired commands   
    args = parser.parse_args()

    if (args.cmd == target.COMMAND):
        target.run(args, parser)
    elif (args.cmd == solve.COMMAND):
        solve.run(args, parser)
    elif (args.cmd == verify.COMMAND):
        verify.run(args, parser)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

