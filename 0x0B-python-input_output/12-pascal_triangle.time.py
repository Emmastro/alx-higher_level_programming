#!/usr/bin/python3
""" pascal triangle"""
import time

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp


def unix_time(function):
    '''Return `real`, `sys` and `user` elapsed time, like UNIX's command `time`
    You can calculate the amount of used CPU-time used by your
    function/callable by summing `user` and `sys`. `real` is just like the wall
    clock.
    Note that `sys` and `user`'s resolutions are limited by the resolution of
    the operating system's software clock (check `man 7 time` for more
    details).
    '''
    print("test: {}".format(function.__name__))
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    function()
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()

    print("\nreal: {}\nuser: {}\nsys: {}\n".format(
        end_time - start_time,
        end_resources.ru_utime - start_resources.ru_utime,
        end_resources.ru_stime - start_resources.ru_stime)
    )


def pascal_triangle(n=4500):
    """print pascal"""
    pascal = [[0]*i for i in range(1,n+1)]
    cmpt = 0
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(0, i//2):
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
            pascal[i][i-j-1] = pascal[i-1][j] + pascal[i-1][j+1]
            cmpt+=1
    print("loop:", cmpt)
    return pascal

def pascal_triangle1(n=4500):
    """print pascal"""
    pascal = [[0]*i for i in range(1,n+1)]
    cmpt = 0
    for i in range(n):
        pascal[i][0] = 1
        pascal[i][-1] = 1
        for j in range(0, i-1):
            pascal[i][j+1] = pascal[i-1][j] + pascal[i-1][j+1]
            cmpt += 1
    print("loop:", cmpt)
    
    return pascal


unix_time(pascal_triangle1)
unix_time(pascal_triangle1)
unix_time(pascal_triangle)
unix_time(pascal_triangle)