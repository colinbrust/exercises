from math import lcm
from fractions import Fraction
expression = "-5/2+10/3+7/9"

def frac_add(expression):
    nums = []
    denoms = []
    idx = 0
    while True:

        try:
            nchar = 3 if expression[idx].isnumeric() else 4
            frac = expression[idx:idx+nchar]
            frac = frac.split("/")
            nums.append(int(frac[0]))
            denoms.append(int(frac[1]))
            idx = idx + nchar
        except IndexError:
            break

    fracs = list(zip(nums, denoms))
    mult = lcm(*denoms)

    total = 0
    for num, denom in fracs:
        total += num * mult/denom

    out = Fraction(int(total), int(mult))

    return f"{out.numerator}/{out.denominator}"