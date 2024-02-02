#author: Jay Sanders

import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(help="String entered:", dest="inString", type=str)
    parser.add_argument(help="Integer entered:", dest="inInt", type=int)
    parser.add_argument(help="Float entered:", dest="inFloat", type=float)

    args = parser.parse_args()

    #print(args.inString, args.inInt, args.inFloat)

if __name__ == "__main__":
    main()