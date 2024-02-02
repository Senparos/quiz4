#author: Jay Sanders
from dataclasses import dataclass

@dataclass
class Song:
    name : str
    artist: str
    genre : str
    released : int
def main():
    song1 = Song("Never Meant", "American Football", "Midwest Emo", 1999)
    
    # print(song1.artist)
    # print(song1.name)
    # print(song1.genre)
    # print(song1.released)

if __name__ == "__main__":
    main()