#author: Jay Sanders
from datetime import datetime

def currTime() -> str:
    time = datetime.now()
    return time.strftime("%H:%M:%S")