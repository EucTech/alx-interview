#!/usr/bin/python3
"""pascal triangle"""

def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []
    
    tri_value = [[1]]
    
    for val in range(1, n):
        tri = [1]
        for k in range(val):
            tri.append(tri_value[val - 1][k - 1] + tri_value[val - 1][k])
        tri.append(1)
        tri_value.append(tri)

    return tri_value
