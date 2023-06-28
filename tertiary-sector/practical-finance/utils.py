import numpy as np


class RangeDict(dict):
    """
    Custom dictionary class to use key ranges in the form of key[0] < item < key[1] as keys.
    """

    def __getitem__(self, item):
        if not isinstance(item, tuple):
            for key in self:
                if key[0] < item < key[1]:
                    return self[key]
        else:
            return super().__getitem__(item)

if __name__ == '__main__':
    a = RangeDict({(0.1, 1): "Test"})
    print(a[0.5])