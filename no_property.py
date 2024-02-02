#author: Jay Sanders

class Band:
    def __init__(self, name : str, hometown : str):
        self.nameVal = name
        self.hometownVal = hometown
    def setName(self, name) -> None:
        self.nameVal = name
    def getName(self) -> str:
        return self.nameVal
    def setHometown(self, hometown) -> None:
        self.hometownVal = hometown
    def getHometown(self) -> str:
        return self.hometownVal
def main():
    band1 = Band("Title Fight", "Kingston, Pennsylvania")
    # print(f"{band1.getName()} is from {band1.getHometown()}")
    band1.setName("Glitterer")
    # print(f"{band1.getName()} is from {band1.getHometown()}")
if __name__ == "__main__":
    main()