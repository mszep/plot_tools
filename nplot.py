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

def main(infile):

    arr = scipy.loadtxt(sanitized(infile))
    
    if len(sys.argv) > 1:
        xaxis, yaxis = [int(i) -1 for i in sys.argv[1].split(':')]
        plt.plot(arr[:,xaxis], arr[:,yaxis])
    else:
        for i in range(1, a.shape[1]):
            plt.plot(arr[:,0], arr[:,i])

    plt.show()

if __name__ == '__main__':
    main(sys.stdin)
