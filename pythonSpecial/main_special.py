#This is the main program to invoke the practice scripts
from pythonSpecial.counters import main_counter
from pythonSpecial.generators import main_gen
from pythonSpecial.decorators import main_dec


def main_special():
    # this is the entry function for decorators testing
    main_dec()

    # this is the entry function for generators testing
    main_gen()

    # this is the entry function for counters testing
    main_counter()