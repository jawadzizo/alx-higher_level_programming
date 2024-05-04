#!/usr/bin/python3
"""Module to multiply 2 matrices
"""


def check_matrix_multiplication(m_a, m_b):
    """checks the conditions of matrix multiplication"""

    # check if the matrices are lists
    if isinstance(m_a, list) is False:
        raise TypeError("m_a must be a list")
    if isinstance(m_b, list) is False:
        raise TypeError("m_b must be a list")

    # check if the matrices are lists of lists
    if all(isinstance(sub_list, list) for sub_list in m_a) is False:
        raise TypeError("m_a must be a list of list")
    if all(isinstance(sub_list, list) for sub_list in m_b) is False:
        raise TypeError("m_b must be a list of list")

    # check if matrices are empty
    if len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # check if list contains only integers or floats
    for sub_list in m_a:
        if all(type(element) in [int, float] for element in sub_list) is False:
            raise TypeError("m_a should contain only integers or floats")
    for sub_list in m_b:
        if all(type(element) in [int, float] for element in sub_list) is False:
            raise TypeError("m_b should contain only integers or floats")

    # check if matrices are rectangle
    if all(len(sub_list) == len(m_a[0]) for sub_list in m_a) is False:
        raise TypeError("each row of m_a must be of the same size")
    if all(len(sub_list) == len(m_b[0]) for sub_list in m_b) is False:
        raise TypeError("each row of m_b must be of the same size")

    # check if the multiplication is possible
    if (len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")


def matrix_mul(m_a, m_b):
    """multiplies 2 matrices"""

    check_matrix_multiplication(m_a, m_b)

    matrix = []

    for row_a in m_a:
        tmp = []
        for i in range(len(m_b[0])):
            j = 0
            sum_cell = 0
            for element in row_a:
                sum_cell += element * m_b[j][i]
                j += 1

            tmp.append(sum_cell)
        matrix.append(tmp)

    return (matrix)
