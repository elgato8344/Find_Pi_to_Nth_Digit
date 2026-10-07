## Todo - Find PI to the Nth Digit - Enter a number and have the program generate
## Todo - PI up to that many decimal places. Keep a limit to how far the program will go.
from decimal import Decimal, getcontext
import math
from random import randint
import textwrap

def calc_pi(n):
    """easiest way to calculate pi since math module limits us to 15 decimal places is to use
    Chudnovsky algorithm which I read about on https://en.wikipedia.org/wiki/Chudnovsky_algorithm"""
    if n < 1:
        return "3"
    # working precision to avoid rounding errors at the final digits
    getcontext().prec = n + 5
    # calc number of iterations needed (approx 14 per term)
    iters_1 = math.ceil(n / 14) + 1
    # constants
    C = 426880 * Decimal(10005).sqrt()
    M = 1
    L = 13591409
    X = 1
    K = 6
    S = Decimal(L)

    for k in range(1, iters_1):
        # most efficient way I can calc the next terms using recurrence relations
        M = (M * (K**3 - 16*K)) // (k**3)
        L += 545140134
        X *= -262537412640768000
        S += Decimal(M * L) / Decimal(X)
        K += 12
    pi = C / S
    pi_string = str(pi)
    return pi_string[:n + 2] # +2 account for "3"

def get_balanced_width(total_length, target_width=30):
    """using this to find a width closest to target so it prints as cleanly as possible.
    if length has no perfect divisor, defaults back to target"""
    best_width = target_width
    smallest_remainder = target_width
    # checks widths 15-60 to find balanced option since Nth digit is a random number
    for possible_width in range(15, 61):
        remainder = total_length % possible_width
        # remainder of 0 is a perfectly even row
        if remainder == 0:
            return possible_width
        # if not perfect, looks for option with smallest leftover chunk
        if remainder < smallest_remainder:
            smallest_remainder = remainder
            best_width = possible_width
    return best_width

def main():
    digits = randint(1, 1000)
    pi_string = calc_pi(digits)
    total_pi_length = len(pi_string)
    dynamic_width = get_balanced_width(total_pi_length, target_width=30)
    final_result = textwrap.wrap(calc_pi(digits), width=dynamic_width)

    print(f"# of digits to display: {digits}")
    print("result: ")
    print("\n".join(final_result))

if __name__ == "__main__":
    main()