from enum import Enum

class FileStatus(Enum):
    CONVERTED = "Converted"
    UNCONVERTED = "Unconverted"
    NOT_SUPPORTED = "Not supported"
    CONVERTING = "Converting"