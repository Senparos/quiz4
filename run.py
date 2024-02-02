#author: Jay Sanders
from module1.mod1 import currTime
from module2.mod2 import directory
from module3.mod3 import formatEntry

def main():
    print(formatEntry(currTime(), directory()))
if __name__ == "__main__":
    main()