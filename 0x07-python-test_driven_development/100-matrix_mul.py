#!/usr/bin/python3


def matrix_mul(m_a, m_b):
    """Multiply two matrices"""

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    len1 = len(m_a)
    if len1 == 0:
        raise ValueError("m_a can't be empty")
    len2 = None
    for i in m_a:
        if type(i) is not list:
            raise TypeError("m_a must be a list of lists")
        if len2 is None:
            len2 = len(i)
            if len2 == 0:
                raise ValueError("m_a can't be empty")
        if len2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    len3 = None
    for i in m_b:
        if type(i) is not list:
            raise TypeError("m_b must be a list of lists")
        if len3 is None:
            len3 = len(i)
            if len3 == 0:
                raise ValueError("m_b can't be empty")
        if len3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if len2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(len1):
        leng = []
        for j in range(len3):
            n = 0
            for m in range(len2):
                n += m_a[i][m] * m_b[m][j]
            leng.append(n)
        matrix.append(leng)
    return matrix
