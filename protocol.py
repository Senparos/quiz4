#author: Jay Sanders
from typing import Protocol

class Musician(Protocol):
    def setName(self, name : str) -> None:
        pass
    def getName(self) -> str:
        pass
class Drummer:
    def __init__(self, name : str, drums : str):
        self.name = name
        self.drums = drums
    def setName(self, name: str) -> None:
        self.name = name
    def getName(self) -> str:
        return self.name
    def setDrum(self, drums : str) -> None:
        self.drums = drums
    def getDrum(self) -> str:
        return self.drums
    def drum(self) -> str:
        return f"{self.name} is drumming on {self.drums} drums"
class Guitarist:
    def __init__(self, name : str, guitar : str):
        self.name = name
        self.guitar = guitar
    def setName(self, name : str) -> None:
        self.name = name
    def getName(self) -> str:
        return self.name
    def setGuitar(self, guitar : str) -> None:
        self.guitar = guitar
    def getGuitar(self) -> str:
        return self.guitar
    def strum(self) -> str:
        return f"{self.name} is playing their {self.guitar} guitar"
def main():
    player1 : Musician = Drummer("Herb Alexander", "Tama")
    player2 : Musician = Guitarist("Larry Lalonde", "Fender")

    # print(player1.drum())
    # print(player2.strum())
if __name__ == "__main__":
    main()