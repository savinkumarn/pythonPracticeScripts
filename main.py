#This is the main program to invoke the practice scripts
from decorators import main_dec
from generators import main_gen
from counters import main_counter

def main():
    #this is the entry function for decorators testing
    #main_dec()

    #this is the entry function for generators testing
    #main_gen()

    #this is the entry function for counters testing
    main_counter()

if __name__ == '__main__':
    main()