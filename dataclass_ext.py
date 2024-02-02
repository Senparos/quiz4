#author: Jay Sanders
from dataclasses import dataclass

@dataclass
class Song:
    name : str
    artist: str
    genre : str
    released : int
    def printEntry(self) -> str:
        return f"The song {self.name} was released in {self.released} by {self.artist}, and is in the {self.genre} genre"
def main():
    song1 = Song("Pink Moon", "Nick Drake", "Singer-Songwriter", 1972)
    
    # print(song1.printEntry())

if __name__ == "__main__":
    main()