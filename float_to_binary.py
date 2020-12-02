from math import copysign, fabs, isfinite, modf


# Функция, возращающая дробную часть числа 
# в двоичной системе счисления
def floatToFracBin(f):
    if not isfinite(f):
        return repr(f)

    frac = fabs(f)%1
    n, d = frac.as_integer_ratio()
    assert d & (d - 1) == 0
    return f'{n:0{d.bit_length()-1}b}'