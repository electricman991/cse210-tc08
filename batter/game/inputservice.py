import sys
from game.point import Point
from asciimatics.event import KeyboardEvent

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
        _keys (list): Points for left, right.
    """
    