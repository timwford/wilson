from enum import Enum


class Motion(Enum):
    FORWARD = 'F'
    BACKWARD = 'B'
    LEFT = 'L'
    RIGHT = 'R'
    HALT = 'H'

class Sound(Enum):
    LOW_SLOW = 'V'
    HIGH_SLOW = 'X'
    LOW_FAST = 'Y'
    HIGH_FAST = 'Z'


motions = [m.value for m in Motion]
sounds = [m.value for m in Sound]
