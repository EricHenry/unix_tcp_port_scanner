import argparse

parser = argpars.ArgumentParser()
parser.add_argument('-H', '--hostname', help='specify target host')
parser.add_argument('-p', '--port', help='specify target port')
args = parser.parse_args()

if not (args.hostname and args.port):
    parser.print_help()
    exit(0)

def main(hostname, port):
    pass

if __name__ == '__main__':
    main(args.hostname, args.port)
