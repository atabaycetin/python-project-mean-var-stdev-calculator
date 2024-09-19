import numpy as np
from pprint import pprint


def calculate(_list):
    if len(_list) != 9:
        raise ValueError('List must contain nine numbers.')
    calculations = dict()
    a = np.array(_list).reshape(3, 3)

    calculations['mean'] = [[a[range(3), 0].mean(), a[range(3), 1].mean(), a[range(3), 2].mean()], [a[0].mean(), a[1].mean(), a[2].mean()], a.mean()]

    calculations['variance'] = [[a[range(3), 0].var(), a[range(3), 1].var(), a[range(3), 2].var()], [a[0].var(), a[1].var(), a[2].var()], a.var()]

    calculations['standard deviation'] = [[a[range(3), 0].std(), a[range(3), 1].std(), a[range(3), 2].std()], [a[0].std(), a[1].std(), a[2].std()], a.std()]

    calculations['max'] = [[a[range(3), 0].max(), a[range(3), 1].max(), a[range(3), 2].max()], [a[0].max(), a[1].max(), a[2].max()], a.max()]

    calculations['min'] = [[a[range(3), 0].min(), a[range(3), 1].min(), a[range(3), 2].min()], [a[0].min(), a[1].min(), a[2].min()], a.min()]

    calculations['sum'] = [[a[range(3), 0].sum(), a[range(3), 1].sum(), a[range(3), 2].sum()], [a[0].sum(), a[1].sum(), a[2].sum()], a.sum()]

    return calculations


if __name__ == "__main__":
    df = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]).reshape(3, 3))
    pprint(df)
