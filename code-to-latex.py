import sys

def main():

    # accept arguments
    infilename = sys.argv[1]
    outfilename = sys.argv[2]

    # open file streams
    infile = open(infilename, 'r')
    outfile = open(outfilename, 'w')

    lines = infile.readlines()
    for line in lines:
        outfile.write('\\verb|' + line.replace('\n', '') + '|\\\\\n')

    

if __name__ == "__main__":
    main()