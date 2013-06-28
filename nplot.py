#!/bin/env python

import scipy
import matplotlib.pyplot as plt
import sys

def sanitized(input):
    for line in input:
        if line.strip() == '':
            continue
        try:
            dummy = scipy.loadtxt([line])
            yield line
        except ValueError:
            pass

def main(infile, cols_list=[]):
    arr = scipy.loadtxt(sanitized(infile))
    if cols_list == []:
        for i in range(1, arr.shape[1]):
            cols_list.append((0, i))
    for cols in cols_list:
        plt.plot(arr[:,cols[0]], arr[:,cols[1]])
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) > 2:
        sys.exit('Error; too many command line arguments')
    elif len(sys.argv) == 2:
        cols = tuple([int(i) -1 for i in sys.argv[1].split(':')])
        main(sys.stdin, [cols])
    else:
        main(sys.stdin)
