#author: Jay Sanders

class Band:
    def __init__(self, name : str, hometown : str):
        self.nameVal = name
        self.hometownVal = hometown
    @property
    def name(self) -> str:
        return self.nameVal
    @name.setter
    def name(self, newName) -> None:
        if not isinstance(newName, str):
            n, h = newName
        else:
            n = newName
            h = "N/A"
        self.nameVal = n
        self.hometownVal = h
def main():
    band1 = Band("Title Fight", "Kingston, Pennsylvania")
    print(f"{band1.name} is from {band1.hometownVal}")
    band1.name = "Glitterer"
    print(f"{band1.name} is from {band1.hometownVal}")
if __name__ == "__main__":
    main()