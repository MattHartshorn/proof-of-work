from . import sha256

COMMAND = "verify"

def verify(data, solution, target):
    """Verifies that the provided solution is a valid POW for the given data and difficulty
    Arguments:
    data --  The binary data that is hashed
    target -- The POW difficulty value, in bytes
    solution -- The value used to validate that work was done

    Returns:
    True if the provided solution value is valid, otherwise False
    """
    hashcode = sha256.hash(data, solution)
    return hashcode <= target

def setup(parsers):
    parser = parsers.add_parser(COMMAND, help="Checks if the provided solution is satisfies the difficulty requirements from the given target")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", help="The input file that will be hashed", metavar="FILE")
    group.add_argument("-m", "--message", help="The input message that will be hashed", metavar="MSG")

    parser.add_argument("solution", help="The file that contains the POW solution value")   
    parser.add_argument("target", help="The file that contains the diffulty target")   
    return parsers

def readData(args, parser):
    # Read the input data ot bytes
    data = args.message
    if (data != None): return data.encode()

    try:
        with open(args.input, "rb") as fs:
            return fs.read()
    except Exception as ex:
        print("ERROR -- ", ex)
        parser.error("Failed to read input file")

def readTarget(args, parser):
    # Read the target data to bytes
    try:
        with open(args.target, "r") as fs:
            return bytes.fromhex(fs.read())
    except Exception as ex:
        print("ERROR --", ex)
        parser.error("Failed to read target file")

def readSolution(args, parser):
    # Read the solution data to bytes
    try:
        with open(args.solution, "r") as fs:
            return int(fs.read())
    except Exception as ex:
        print("ERROR --", ex)
        parser.error("Failed to read solution file")

def run(args, parser):
    data = readData(args, parser)
    solution = readSolution(args, parser)
    target = readTarget(args, parser)

    print("1 (valid)" if verify(data, solution, target) else "0 (invalid)")