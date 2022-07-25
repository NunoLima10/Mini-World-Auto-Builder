
class FileNotFoundException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PalletSizeException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class VoxPaserException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class VoxHasNoPalleteException(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
