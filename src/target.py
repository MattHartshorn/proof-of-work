
COMMAND = "target"

def generate(difficulty):
    """Generates the proof-of-work target as bytes
    Arguments:
    difficulty -- The number of bits that are required to be zeros, 0 - 256 

    Returns:
    bytes that represent the desired target 
    """
    if (difficulty < 0 or difficulty > 256):
        raise ValueError("The difficulty must be between 0 and 256")

    target = "0" * difficulty + "1" * (256 - difficulty)
    return bytes(int(target[i : i + 8], 2) for i in range(0, len(target), 8))

def setup(parsers):
    parser = parsers.add_parser(COMMAND, help="Generates the POW target value")
    parser.add_argument("-o", "--output", help="The file in which the output will be written", metavar="FILE")
    parser.add_argument("difficulty", help="The number of bits to be set to zero for the target difficulty", type=int)
    return parsers

def run(args, parser):
    # Generate the target value
    target = None
    try:
        target = generate(args.difficulty).hex()
    except ValueError as ex:
        parser.error(str(ex))
        return

    # Write the output target
    if (args.output == None): 
        print(target)
    else:
        try:
            with open(args.output, "w") as fs:
                fs.write(target)
        except Exception as ex:
            print("Failed to write to output file")
            print("ERROR -- ", ex)