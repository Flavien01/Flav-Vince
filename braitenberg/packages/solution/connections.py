from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    height, width = shape
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, :width//2]=1
    res[:, width//2:]=-1
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    height, width = shape
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    res[:, width//2:]=1
    res[:, :width//2]=-1
    # ---
    return res
