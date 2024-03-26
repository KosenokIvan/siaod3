class VeryBigNumber:
    def __init__(self):
        pass

    def __add__(self, other):
        return VeryBigNumber()

    def __radd__(self, other):
        return VeryBigNumber()

    def __lt__(self, other):
        return False

    def __le__(self, other):
        return False

    def __gt__(self, other):
        return True

    def __ge__(self, other):
        return True
