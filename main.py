import numpy as np
import decimal


def lista_liczb(a, b):

    lista = np.arange(a, b, 0.5, dtype=np.dtype(decimal.Decimal))
    return lista


lista_liczb(2, 5.5)
