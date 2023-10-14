"""
My Test Program
"""

def count_set_bits(number):
    """
    Count the number of bits which are set one
    """
    return bin(number)[2:].count("1")
