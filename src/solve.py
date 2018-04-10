from . import sha256

COMMAND = "solve"

def solve(data, target):
    """Hashes the provided data and attempts to find a viable solution for the provided POW target
    Arguments:
    data --  The binary data that is hashed
    target -- The POW difficulty value, in bytes

    Returns:
    The binary hashcode and solution for the provided POW target
    """
    if(not isinstance(data, bytes)):
        raise TypeError("data must be of type 'bytes'")
    if(not isinstance(target, bytes)):
        raise TypeError("target must be of type 'bytes'")

    solution = 0
    hashcode = sha256.hash(data, solution)
    while hashcode > target:
        solution += 1
        hashcode = sha256.hash(data, solution)

    return (hashcode, solution)


def setup(parsers):
    parser = parsers.add_parser(COMMAND, help="Attempts to solve the POW problem given input data and a target difficulty")
    parser.add_argument("-o", "--output", help="The file in which the output will be written", metavar="FILE")
    
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-i", "--input", help="The input file that will be hashed", metavar="FILE")
    group.add_argument("-m", "--message", help="The input message that will be hashed", metavar="MSG")

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

def writeOutput(data, hashcode, solution, args, parser):
    # Write the output
    if (args.output == None):
        try:
            print("Data:", data.decode("utf-8"))
            print("=" * 80)
        except:
            pass
        print("Hash:", hashcode.hex())
        print("Solution:", solution)
    else:
        try:
            with open(args.output, "w") as fs:
                fs.write(str(solution))
        except Exception as ex:
            print("ERROR --", ex)
            parser.error("Failed to write to output file")

def run(args, parser):
    data = readData(args, parser)
    target = readTarget(args, parser)

    # Attempt to solve the POW 
    hashcode, solution = solve(data, target)

    writeOutput(data, hashcode, solution, args, parser)