import numpy as np


def generate_parallel_shocks():

    return np.arange(
        -100,
        105,
        5
    )


def bps_to_decimal(bps):

    return bps / 10000
