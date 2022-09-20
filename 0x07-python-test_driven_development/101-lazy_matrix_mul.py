#!/usr/bin/python3
"""
Defines lazy_matrix function
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """ calculates the matrix multiplication of two matrices"""
    re = numpy.matmul(m_a, m_b)
    return re
