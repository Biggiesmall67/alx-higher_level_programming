#!/usr/bin/python3
""" use numpy to multiply two matrices in a lazy way"""
import numpy as np


def lazy_matrix_mul(m_c, m_d):
        """ Function that takes 2 matrices and multiplies them

        Args:
            m_c: first matrix
            m_d: second matrix

        Return: the product of m_c and m_d
        """
        return np.matmul(m_c, m_d)
